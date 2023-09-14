#env python3

import os
import json
import yaml

import frontmatter
from slugify import slugify

import datetime
import dateutil.parser
from pytz import timezone

from pprint import pprint

import requests

from datetime import datetime

from os import environ
access_token_key = environ.get('ACCESS_TOKEN_KEY')

HEADERS = {'Authorization': f'Token {access_token_key}'}


def logging():
    import logging

    # These two lines enable debugging at httplib level (requests->urllib3->http.client)
    # You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
    # The only thing missing will be the response.body which is not logged.
    try:
        import http.client as http_client
    except ImportError:
        # Python 2
        import httplib as http_client
    http_client.HTTPConnection.debuglevel = 1

    # You must initialize logging, otherwise you'll not see debug output.
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

def main():

    #logging()

    today = datetime.today().strftime('%Y-%m-%d')
    event = "bsidesmunich2023" # The current conference slug

    with requests.Session() as s:
        s.headers = HEADERS

        #res = s.get(f'https://pretalx.com/api/events/{event}/')
        res = s.get(f'https://pretalx.com/api/me')
        #jdata = res.json()
        jdata = res.json()
        pprint(res.json())
        if res.status_code == 401:
            print('401 - {}'.format(jdata['detail']))
            return
        #input()
        #pprint(jdata)


        speakers = None
        filename = f'_data/{today}_speakers.json'
        if os.path.isfile(filename):
            with open(filename, 'r') as infile:
                speakers = json.load(infile)

        else:

            #res = s.get(f'https://pretalx.com/api/events/{event}/')
            res = s.get(f'https://pretalx.com/api/me')
            #jdata = res.json()
            #pprint(res)
            #pprint(jdata)

            #res = s.get(f'https://pretalx.com/api/events/{event}/talks')
            res = s.get(f'https://pretalx.com/api/events/{event}/speakers/')
            jdata = res.json()
            jdata_speakers = jdata['results']
            while 'next' in jdata and jdata['next'] is not None:
                # load next page
                pprint(jdata['next'])
                res = s.get(jdata['next'])
                jdata = res.json()
                
                jdata_speakers = jdata_speakers + jdata['results']
            
            #pprint(jdata_speakers)

            filename = f'_data/{today}_speakers.json'
            with open(filename, 'w') as outfile:
                json.dump(jdata_speakers, outfile, indent=4, sort_keys=True)
                
                speakers = jdata_speakers


        sessions = None
        filename = f'_data/{today}_sessions.json'
        if os.path.isfile(filename):
            with open(filename, 'r') as infile:
                sessions = json.load(infile)
        else:

            #res = s.get(f'https://pretalx.com/api/events/{event}/talks')
            res = s.get(f'https://pretalx.com/api/events/{event}/submissions')
            jdata = res.json()
            jdata_sessions = jdata['results']
            while 'next' in jdata and jdata['next'] is not None:
                # load next page
                pprint(jdata['next'])
                res = s.get(jdata['next'])
                jdata = res.json()
                
                jdata_sessions = jdata_sessions + jdata['results']
            
            #pprint(jdata_sessions)

            sessions_filtered = []
            for session in jdata_sessions:
                #pprint(session)
                #pprint(session['state'])

                if session['state'] == 'accepted':
                    sessions_filtered.append(session)
                elif session['state'] == 'confirmed':
                    sessions_filtered.append(session)
                elif session['state'] == 'rejected':
                    continue
                elif session['state'] == 'submitted':
                    continue
                elif session['state'] == 'withdrawn':
                    continue
                elif session['state'] == 'canceled':
                    continue

                else:
                    pprint(session)
                    pprint(session['state'] )
                    input()

            with open(filename, 'w') as outfile:
                json.dump(sessions_filtered, outfile, indent=4, sort_keys=True)

                sessions = sessions_filtered

    track_cnt = {}

    # Testing
    for session in sessions:
        #print(session['slot'])
        
        if session['slot'] is None:
            pprint(session)
    
    #newlist = sorted(list_to_be_sorted, key=lambda d: d['name']) 
    #sessions_sorted = sorted(sessions, key=lambda d: d['Start']) 
    sessions_sorted = sorted(sessions, key=lambda d: d['slot']['start']) 
    for session in sessions_sorted:
        #pprint(session)
        
        metadata = yaml.dump(session)
        session_str = f'---\n{metadata}\n---\n{session["abstract"]}'
        #print(session_str)
        #post = frontmatter.loads(session_str)
        post = frontmatter.loads('')
        #print(post)
        post_abstract = session['abstract']
        post_abstract = post_abstract.replace('. ', '.\n')
        post_abstract = post_abstract.replace('\r\n', '\n')
        post_description = session['description']
        post_description = post_description.replace('. ', '.\n')
        post_description = post_description.replace('\r\n', '\n')
        
        post.content = post_abstract
        #post.content = post_abstract + '\n\n' + post_description
        #post.content = post.content + '\n\n' + session['Description'].replace('. ', '.\n')

        print(session['submission_type'])
        post['layout'] = session['submission_type']['en'].lower().split(" ")[0]

        if post['layout'] == 'talks':
            post['layout'] = 'talk'

        if session['state'] == 'accepted':
            post['accepted'] = True
        elif session['state'] == 'confirmed':
            post['accepted'] = True
            
        post['keynote'] = session['is_featured']
        #post['details'] = session['details']
        post['track'] = session['slot_count']
        post['title'] = session['title']
        post['code'] = session['code']

        post['details'] = True

        NYC = timezone('America/New_York')        
        MUC = timezone('Europe/Berlin')        
        post['timeslot'] = {}
        post['timeslot']['start'] = session['slot']['start'] # convert to timestamp
        dt_start = dateutil.parser.parse(session['slot']['start'])
        dt_start_here = dt_start.astimezone(MUC)
        post['timeslot']['start'] = dt_start_here

        post['timeslot']['end'] = session['slot']['end'] # convert to timestamp
        #end_here = pytz.utc.localize(dateutil.parser.parse(session['Start']))
        dt_end = dateutil.parser.parse(session['slot']['end'])
        dt_end_here = dt_end.astimezone(MUC)
        post['timeslot']['end'] = dt_end_here
        post['timeslot']['duration'] = session['duration']
        
        session_speakers = []
        for sess_speaker in session['speakers']:

            for speaker in speakers:

                if 'code' not in speaker:
                    pprint(speaker)
                    input('speaker')

                elif 'code' not in sess_speaker:
                    pprint(sess_speaker)
                    pprint(session)
                    input('sess_speaker')

                print(f'{sess_speaker["code"]} vs {speaker["code"]}')
                if speaker['code'] == sess_speaker['code']:
                    session_speaker = {}
                    session_speaker['name'] = speaker['name']
                    session_speaker['handle'] = False # speaker[''] This is not exported from pretalx
                    session_speaker['bio'] = speaker['biography']
                    session_speaker['photo'] = speaker['avatar']
                    session_speakers.append(session_speaker)

                    break

        post['speakers'] = session_speakers

        if session['track']['en'] == 'Workshops':
            post_folder = '_workshops'
        elif session['track']['en'] == 'Talks':
            post_folder = '_talks'
        else:
            post_folder = session['track']['en']
            print('#'*10)
            print(post_folder)
            input()

        if session['slot']['room']['en'] == 'Hochschule - Room 1':
            post['track'] = 1
        elif session['slot']['room']['en'] == 'Hochschule - Room 2':
            post['track'] = 2
        elif session['slot']['room']['en'] == 'Hochschule - Room 3':
            post['track'] = 3
        elif session['slot']['room']['en'] == 'Hochschule - Room 4':
            post['track'] = 4
        elif session['slot']['room']['en'] == 'WestIn - Munich':
            post['track'] = 1
        elif session['slot']['room']['en'] == 'WestIn - Partenkirchen':
            post['track'] = 2
        else:
            post['track'] = session['slot']['room']['en']
            print('#'*10)
            print(frontmatter.dumps(post))
            input()


        if post_folder not in track_cnt:
            track_cnt[post_folder] = {}

        if post['track'] not in track_cnt[post_folder]:
            track_cnt[post_folder][post['track']] = 1
        else:
            track_cnt[post_folder][post['track']] += 1

        #print('#'*10)
        #pprint(post)
        #input()
        #print('#'*10)
        #print(frontmatter.dumps(post))

        # Sort by file name? {slot}-{talkno}_{title}.md
        session_id = track_cnt[post_folder][post['track']]
        #filename = f"{post['track']:03}-{session_id:02}_{slugify(post['title'])}.md"
        filename = f"{post['track']:03}-{session_id:02}_{post['code']}_{slugify(post['title'])}.md"

        filepath = f'{post_folder}/{filename}'
        print('#'*10)
        print(filepath)
        #input()
        # Check if session exists
        #if not os.path.exists(filepath):
        with open(filepath, 'w') as fh:
            fh.write(frontmatter.dumps(post))

if __name__ == '__main__':
    main()
