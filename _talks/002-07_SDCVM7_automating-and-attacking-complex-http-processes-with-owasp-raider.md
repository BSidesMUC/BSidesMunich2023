---
accepted: true
code: SDCVM7
details: true
keynote: false
layout: talk
speakers:
- bio: "Daniel is a seasoned pentester with over 5 years of experience in\r\nsecurity,
    5 more as a sysadmin, and a passion for building tools that\r\nsolve real-world
    problems. His experience helping developers build\r\nOAuth directly from RFCs
    highlighted the limitations of existing\r\ntools, motivating him to build a more
    flexible and customizable\r\nsolution. 2 years ago, he started building Raider,
    and later the same\r\nyear it became a part of OWASP, and he's been actively developing
    and\r\nimproving raider ever since."
  handle: false
  name: Daniel Neagaru
  photo: ''
timeslot:
  duration: 30
  end: 2023-10-15 15:00:00+02:00
  start: 2023-10-15 14:30:00+02:00
title: Automating and attacking complex HTTP processes with OWASP Raider
track: 2
---

Raider is a novel, LISP-based framework for web application security
testing that abstracts the client-server information exchange as a
finite state machine.
Each step comprises one request with inputs, one
response with outputs, arbitrary actions to do on the response, and
conditional links to other stages, creating a graph-like
structure.
This architecture works not only for authentication
purposes but can be used for any HTTP process that needs to keep track
of states.
In this presentation, we'll cover the motivation behind
Raider, the key concepts of the framework, and demonstrate how it can
automate complex HTTP processess.
We'll show how Raider's flexibility
enables easy customization of attacks and how its clear text
configuration makes reproducing, sharing, and modifying attacks easy.