---
accepted: true
code: XSMDVT
details: true
keynote: false
layout: talk
speakers:
- bio: Daniel Feichter is 37 years old, from Austria, and known on Twitter and elsewhere
    under the pseudonym VirtualAllocEx. Daniel originally comes from a background
    in electronics and communications engineering and started as a junior penetration
    tester in 2018. With ethical hacking, Daniel found his purpose and can't imagine
    doing anything else since. At the end of 2021, Daniel decided to start his own
    company called RedOps (https://redops.at/en/) (formerly Infosec Tirol) to live
    out his research spirit and focus even more on his main area of interest. Daniel's
    focus is on everything related to malware development, antivirus, endpoint protection,
    endpoint detection and response, and Windows internals. Daniel conducts ongoing
    research in these areas and regularly shares his findings through conference presentations,
    blog posts and workshops. Daniel has presented his research on endpoint detection
    and response, malware development, etc. at conferences such as DEF CON 30 and
    DEF CON 31 Las Vegas, Sans Hackfest 2022 in Arlington, etc. Besides IT security,
    his greatest passion is teaching other infosec professionals around the world.
  handle: false
  name: Daniel Feichter
  photo: https://pretalx.com/media/avatars/C3GT7F_tVTndoz.jpg
timeslot:
  duration: 30
  end: 2023-10-15 10:30:00+02:00
  start: 2023-10-15 10:00:00+02:00
title: '(In)direct Syscalls: A journey from high to low'
track: 1
slides_uri: /files/slides/001-02_XSMDVT - Daniel Feichter_(In)direct Syscalls_ A journey from high to low.pdf
recording_uri: https://www.youtube.com/watch?v=lyYzSKMPD4w&list=PL8N5HiRDvZ-dVdLNXf6kC3WDi8AWBS27g&index=4
---

Over the last 2-3 years, detection of in-memory malware by EDRs has improved.
Depending on the EDR, they use different defenses such as user mode hooks, callbacks, or Event Viewer for Windows (ETW) to detect in-memory threats.
Therefore, among others or depending on the EDR, from an attacker's (red team's) perspective, we must use different types of techniques such as direct sycalls, indirect sycalls, or call stack spoofing to avoid being detected by EDRs.

The goal of this talk is to give a brief, logical overview of syscalls in general on Windows, direct syscalls, indirect syscalls, etc.
We will take a step-by-step look at how to develop a Win32 API shellcode loader into an indirect syscall shellcode loader.
We will go through Win32 APIs, Native APIs, direct syscalls, and indirect syscalls.
We will look at when direct syscalls fail to bypass EDRs and why indirect syscalls are an evolution of direct syscalls and can be used to bypass them, depending on the EDR.
We will also do some call stack analysis and look at the limitations of indirect syscalls in the context of EDR evasion, when they fail, and why it may be necessary to spoof the entire call stack of your shellcode loader to evade an EDR in 2023.