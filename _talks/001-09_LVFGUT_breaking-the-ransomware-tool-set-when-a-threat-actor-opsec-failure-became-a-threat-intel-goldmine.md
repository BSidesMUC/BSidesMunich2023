---
accepted: true
code: LVFGUT
details: true
keynote: false
layout: talk
speakers:
- bio: Nicklas is a Threat Research Analyst, a role that involves much reverse engineering
    and looking into all things malware. Nicklas is also a subject matter expert in
    industrial control systems and anything related to its security. He started his
    career programming PLCs, SCADA systems, and almost anything else possible within
    the industry. Before joining Truesec, Nicklas worked at the Swedish National CERT
    in the Swedish Civil Contingencies Agency.
  handle: false
  name: Nicklas Keijser
  photo: https://pretalx.com/media/avatars/U7W3UP_QNaJnT1.png
timeslot:
  duration: 30
  end: 2023-10-15 16:00:00+02:00
  start: 2023-10-15 15:30:00+02:00
title: Breaking the Ransomware Tool Set – When a Threat Actor Opsec Failure Became
  a Threat Intel Goldmine
track: 1
slides_uri: /files/slides/001-09_LVFGUT - Nicklas Keijser_Breaking the Ransomware Toolset.pdf
recording_uri: https://www.youtube.com/watch?v=SAqqc7jczqQ&list=PL8N5HiRDvZ-dVdLNXf6kC3WDi8AWBS27g&index=10
---

During a recent incident response engagement, I was assigned to reverse engineer the RAT that the threat actor had deployed in the environment.
When analyzing the malware to unpack it, a suspicious string was found in the memory - and ip number with a list.txt .
The list contained a not only a complete inventory that the threat actor had, but also a link to the full repository of all their tools, almost 5 GB / over 100 files and scripts of content covering every part for an intrusion -from reconnaissance to impact and everything in between.
This led to an interesting labyrinth of research on all the aspects of this tooling.