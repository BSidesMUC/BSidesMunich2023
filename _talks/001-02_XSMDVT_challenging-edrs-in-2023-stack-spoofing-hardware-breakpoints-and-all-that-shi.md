---
accepted: true
code: XSMDVT
details: true
keynote: false
layout: talk
speakers:
- bio: Daniel Feichter is 36 years old, comes from Austria and is known on Twitter
    and Co under the pseudonym VirtualAllocEx. Daniel originally comes from the corner
    of electronics and communications engineering and started as a career changer
    as a penetration tester as an employee in 2018. With ethical hacking, Daniel found
    his purpose and since then can't imagine doing anything else. At the end of 2020,
    Daniel decided to found his own company called RedOps (originally Infosec Tirol),
    to fully live out his research spirit and to focus even more on his main area
    of interest. Daniel's focus is on everything related to antivirus, endpoint protection,
    endpoint detection and response and Windows internals. Daniel conducts ongoing
    research in these areas and regularly shares his findings in the form of conference
    presentations or blog posts. Daniel has presented his research results in the
    area of endpoint detection and response, e.g. EDR tampering, at conferences such
    as DeepSec Vienna 2020, BSides Munich 2022, DEFCON 30 Las Vegas (Adversary Village)
    and Sans Hackfest 2022 in Arlington.
  handle: false
  name: Daniel Feichter
  photo: https://pretalx.com/media/avatars/f4ad01758c3e951c7e77cb80882fb6e7_Mc0LrrK.jpg
timeslot:
  duration: 30
  end: 2023-10-15 10:30:00+02:00
  start: 2023-10-15 10:00:00+02:00
title: 'Challenging EDRs in 2023: Stack Spoofing, Hardware Breakpoints and All That
  Shi*'
track: 1
---

In this talk we take a look behind the defences of EDRs in 2023.
Especially the in-memory capabilities of EDRs have improved in the last 2 years or so and red teamers need to think about their strategies and tools.
For example, bypassing AMSI and relying too much on direct syscalls is no longer enough.
The goal of this talk is to go step by step through the defensive mechanisms of EDRs in a logical order based on their historical introduction (AMSI, Inline Hooking, IAT-Hooking, PEB-Hooking, checking return addresses, etc.), explain the mechanisms with understandable details and show possible counter strategies from a red team perspective.
The goal of this talk is to provide a brief understanding of the most important EDRs defensive mechanisms in 2023 and give possible strategies and approaches to deal with them from a red team perspective.