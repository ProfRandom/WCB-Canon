
## Abstract  
**Major Topics:**  
- Explores challenges of interstellar travel across vast distances, starting from sublight limitations (Voyager, relativistic travel).  
- Surveys **FTL drive archetypes** across fiction and theory:  
  - **Warp drive (ST:TOS, ST:TNG, Voyager)** with formulas and time-to-destination calculations.  
  - **Alcubierre metric [sci]:** spacetime bubble mechanics, energy constraints, time dilation consequences.  
  - **Hyperdrives, jump drives, fold engines, wormholes [exo]:** speculative traversal models with narrative implications.  
- Worked worldbuilding examples:  
  - **Vault drive (Serelem Union):** chained jumps with recharge mechanics.  
  - **Kaltai Entente:** civilizational reach limited by FTL lag.  
- Detailed treatment of **relativistic effects**: Lorentz term, time dilation, length contraction, relativistic mass.  
- Implications for **culture, politics, and storytelling**: bioage vs. scope vs. span, asynchronous signals vs. returning ships.  
- Hazards of relativistic travel: **microparticle impacts**, red/blue shift of starlight, radiation exposure.  

**Key Terms & Symbols:**  
- **γ (gamma):** Lorentz factor [sci].  
- **β (beta):** velocity ratio v/c [sci].  
- **Vault drive [neo]:** hypothetical chained-jump FTL with recharge intervals.  
- **Bioage, scope, span [neo]:** narrative distinctions between biological, proper, and chronological age under relativistic effects.  

**Cross-Check Notes:**  
- No collisions with existing canon.  
- Expands **Meta 2 — Math Tools** by applying relativistic equations to travel/narrative contexts.  
- Introduces new [neo] and [exo] terms, but all clearly marked.  
- Serves as a **bridge between real physics (sci) and fictional FTL (exo/neo)** in WCB.  
---
---


# Interstellar Distances
The universe is a very big place — very, very big; okay, very, very, *very* big.

Our Milky Way galaxy comprises a very large volume (from our perspective), most of which is empty space.  The stellar density in the Solar neighborhood is about 0.004 stars per cubic lightyear.  That is to say, on average, every star has 250 cubic light-years of empty space surrounding it.  This equates to a cube 6.3 light-years on a side with the star in the center, or a sphere with a radius of 3.91 light-years.  This seems like a reasonable figure, since the closest star to Sol is Proxima Centauri, at about 4.2 light-years away.

The bright star, Deneb (α Cygni) is 2600 light-years from the Sun.  That's not a long distance compared to the galactic neighborhood (the Andromeda galaxy is 2.5 _million_ light-years away), and certainly not on the scale of the visible universe, which is currently calculated to be 93 **_billion_** light-years across.

If we think about what the term "light-year" actually _means_, we begin to intuit a problem.  A light-year is the distance light travels in one Earth year, so light takes a little under 4 years and 2½ months to get here from there.  Light (the fastest thing in the universe) coming from Deneb takes 2,600 _years_ to reach us from there.  In terms of human timeframes, light we see from Deneb today started its journey here the year Cambyses I became King of Persia.  *Never heard of him?  That's kind-of my point.*

Currently, the most distant human-made object in the universe is Voyager 1, which also has the fastest heliocentric recession speed of any artificial object at about $17$ kilometers per second.  It did its flyby of Saturn in 1980, and NASA officially marksedthe start iof ts journey out of the Solar system on January 1, 1990, almost $35$ years ago, as of this writing.  In that time, it has traversed $168$ Astronomical Units.  One AU is the distance from the Earth to the Sun, which is, on average, $146.9$ million kilometers.  That puts Voyager $25,132,458,000$ (25 _billion_) kilometers away.

That is a distance of $\mathbf{0.0027}$ light-years.  Yes, you read that right.  In $35$ years, Voyager I has covered about $\mathbf{\dfrac{1}{370}}$ of a light-year.  It will take in another $16483.74$ years to travel a full light-year, and when it reaches that distance, there will still be about $3$ light-years of empty space around it in every direction.  It will take $70217.39$ years to reach the distance of Proxima Centauri (though Voyager 1 isn't headed to Proxima Centauri).

Obviously, the propulsion methods we currently have at our disposal are not going to get us to the stars any time soon.

One way to circumvent this problem is to find ways to travel faster than even light does. (Can somebody please quiet down Einstein in the back of the room there?). Drives which accomplish faster-than-light (FTL) velocities have been posited in a wide variety of science fiction novels, movies, television shows, etc. *Hyperdrive*, among the earliest (in film at least) was mentioned in *Forbidden Planet* (1956), (more on thisbelow), but probably the first FTL system to become widely known (and copiously copied) was certainly *Star Trek*'s "warp drive”.

# Warp Drive Is (Woefully) Too Slow
In the Star Trek universe of the *Star Trek: The Original Series* (*ST:TOS*), the speed at which starships could travel was measured in "warp factors", such that warp factor 1 was the exact speed of light. Each succeeding warp factor was calculated by the cube of the warp factor multiplied by the speed of light (c).
$$
v = f^3c
$$
Where:
- $f$ = warp factor number
- v = the speed of the ship in meters/second
- c = the speed of light (299792458 m/s)

If $c$ is taken as 1.0, then $v$ is returned in multiples of lightspeed.  For example

Given:
- $f$ = 3
- $c$ = 1
$$
v = f^3 = 3^3 = 27\; \text{times the speed of light}
$$
- Note that when $c$ = 1, it can be dropped from the equation.

Calculating the warp factor from the speed is a function of the cube-root of the velocity of the ship and the speed of light:
$$
f = \sqrt[3]\frac{v}{c}
$$
- Here, again if one is expressing $v$ as multiples of lightspeed, $c$ is always 1 and the equation can simplify to:
$$
f = \sqrt[3]{v}
$$
## "I'm givin' 'er all she's got, Cap'n!"
The maximum at which Constitution-class ships in *ST:TOS* could travel — and then only for short periods of time — was warp 8, which is a velocity of:
$$
v = f^3 = 8^3 = 512\; \text{times the speed of light}
$$
This seems fast until we start considering actual interstellar distances.

Proxima Centauri is the closest star to the Sun at 4.24 light years distant.  At warp 8, Constitution-class starships take:
$$
T = \frac{4.25}{512} = 0.00828]; \text{years} ≈ 3.025\; \textit{days} 
$$
to make the journey.  Days.  Not minutes; not hours — *days*.

## Boosting The Speed
In *Star Trek: The Next Generation* (*ST:TNG*), the assumption was that warp technology had been improved upon since the days of Kirk and Spock, and warp factors were redefined to be:
$$
v = f^\frac{10}{3}
$$
So now, warp 8 is:
$$
v = f^\frac{10}{3} = 8^\frac{10}{3} = 1024c
$$
… which exactly doubles the old warp 8 velocity and shortens the trip to Proxima Centauri to 1.5124 days, or about 36.3 hours.  Still not an afternoon stroll.

The star Deneb is 2600 lightyears from the Sun.  At *ST:TOS* warp 8, the _Enterprise_ would take
$$
T = \frac{2600}{512} = 5.078\; \textit{years}
$$
to get there.  The *ST:TNG* _Enterprise_, at its warp 8 cuts the trip in half to a mere 2.54 *years*.

And, yet, in the very first episode of *ST:TNG*, "Encounter at Farpoint" (1987), the mission destination is stated to be Deneb IV.  Such a designation is usually assumed to refer to the fourth planet orbiting a star named "Deneb".  Based on this, we can assume Picard and company's destination was the Deneb we just calculated a 2.54 year one-way journey to.

Further more the _Star Trek_ wiki site, Memory Alpha states that "By 2373, the Federation's territory was spread across 8000 lightyears…." Assuming this to be a circular diameter, it would take *ST:TNG Enterprise*
$$
T = \frac{8000}{1024} = 7.8125\; \textit{years}
$$
to traverse the width of the Federation.

- Note: If we take that to mean 8000 *cubic* lightyears, that's a spherical volume of only about
$$
r = \sqrt[3]{\frac{3V}{4\pi}} = \sqrt[3]{\frac{3\cdot8000}{4\pi}} = \sqrt[3]{\frac{24000}{4\pi}} = \sqrt[3]{1909.86} ≈ 12.41\; \text{lightyears}
$$
… in radius, which seems a bit on the small side, doesn't it?

*Star Trek: Voyager (ST:VOY)* used the same warp formula as *ST:TNG*, **up to warp 9**, and then an unspecified exponential curve thereafter, such that warp 10 is infinite velocity.  Most fan sources estimate _Voyager_'s top speed of 9.975 to be 3000c, but that still means that a cross-Federation journey would take:
$$
T = \frac{8000}{3000} = 2.67\; \textit{years}
$$
The Sol-Deneb run mentioned earlier would take:
$$
T = \frac{2600}{3000} = 0.867\; \textit{years} ≈ 316.6\; \textit{days}
$$
… which is just over 10 standard months... and that's *assuming no stops along the course*.

Clearly while _Star Trek_ warp drive is _fast_, interstellar distances make the travel times comparable to steamships crossing the Atlantic in the early 20th Century.

# Other Kinds of Drive Systems
Other franchises have, in fact, made use of far speedier craft.  _The Orville_ frequently uses the term "quantum drive" to describe their FTL drive; _Star Wars_ talks about "hyperdrives"; The _FreeSpace_ game series uses "subspace drive"; the (sadly short-lived) _Dark Matter_ regularly referred to the _Raza_'s "FTL Drive", until they acquired theit "blink drive" (more on this below).

Not all of these go so far as to give actual formulas for calculating drive speeds; _The Orville_ is an exception: captain Ed Mercer mentions in the first season episode "Pria", "We have a ... quantum drive system capable of speeds exceeding 10 light years per hour," which equates to a ST:TOS warp factor of about 44.422.  At that speed, a cross-Federation ship would take the _Orville_ 33.33 days, again something akin to a steamship trip across the Atlantic Ocean.

Let’s see how other universes’ drives stack up when normalized to *Trek*’s warp scale.

| <center>Ship</center>            | <center>Context</center>                      | <center>Top Speed<br>(c)</center><br> | <center>Warp (ST:TOS)</center> | <center>Warp<br>(ST:TNG)</center><br> |
| -------------------------------- | --------------------------------------------- | ------------------------------------: | -----------------------------: | ------------------------------------: |
| Light (for comparison)           | Normal Universe                               |                                     1 |                              1 |                                     1 |
| Alcubierre Metric                | Theorized Normal Universe                     |                                    10 |                           2.15 |                                  2.00 |
| *USCSS Prometheus*               | *Prometheus*                                  |                                  19.5 |                           2.69 |                                  2.44 |
| *FireBall XL5*                   | *Fireball XL5*                                |                                    24 |                           2.88 |                                  2.59 |
| *USCSS Nostromo*                 | *Alien*                                       |                                    44 |                           3.53 |                                  3.11 |
| Whorfin-Class Starships          | *Star Trek VII<br>(Generations)*              |                                    64 |                           4.00 |                                  3.48 |
| *The Ark*                        | *Transformers*                                |                                   115 |                           4.86 |                                  4.15 |
| *USS Enterprise* (NX-01)         | *Star Trek:<br>Enterprise*                    |                                 129.6 |                           5.06 |                                  4.30 |
| D5 Battle Cruiser                | *Star Trek: Enterprise*                       |                                   216 |                           6.00 |                                  5.02 |
| *USS Sulaco*                     | *Aliens*                                      |                                   271 |                           6.47 |                                  5.37 |
| *USS Enterprise* (NCC-1701[-A])  | *Star Trek:<br>The Original Series*           |                                   512 |                           8.00 |                                  6.50 |
| *USS Enterprise* (NCC-1701-B)    | *Star Trek III<br>(The Search for Spock)*     |                                   729 |                           9.00 |                                  7.22 |
| *Pillar of Autumn*               | *Halo*                                        |                                   959 |                           9.86 |                                  7.84 |
| *USS Enterprise* (NCC-1701-D)    | *Star Trek:<br>The Next Generation*           |                                 1,649 |                          11.81 |                                  9.23 |
| *USS Defiant* (NCC-1764)         | *Star Trek:<br>Deep Space Nine*               |                                 1,816 |                          12.20 |                                  9.50 |
| *USS* Voyager                    | *Star Trek:<br>Voyager*                       |                                 2,137 |                          12.88 |                                  9.98 |
| Nomad Probe                      | *Star Trek:<br>The Original Series*           |                                 4,096 |                          16.00 |                                 12.13 |
| Borg Cube                        | *Star Trek<br>(various)*                      |                                 7,912 |                          19.93 |                                 14.77 |
| Prawn Mothership                 | *District 9*                                  |                                11,119 |                          22.32 |                                 16.36 |
| Karla Five Vessel                | *Star Trek:<br>The Animated Series*           |                                46,656 |                          36.00 |                                 25.16 |
| *USS Orville*                    | *The Orville*                                 |                                87,660 |                          44.42 |                                 30.40 |
| *Eagle 5*                        | *Space Balls*                                 |                                89,998 |                          44.81 |                                 30.64 |
| *Ascendant Justice*              | *Halo*                                        |                               333,164 |                          69.32 |                                 45.37 |
| *Moya*                           | *Farscape*                                    |                               365,250 |                          71.48 |                                 46.64 |
| The *GunStar*                    | *The Last Starfighter*                        |                               701,280 |                          88.84 |                                 56.72 |
| The *Intruder*                   | *Valerian and the City of a Thousand Planets* |                               993,480 |                          99.78 |                                 62.97 |
| The *Death Star*                 | *Star Wars<br>(various)*                      |                             1,142,500 |                         104.54 |                                 65.67 |
| *Roger Young*                    | *Starship Troopers*                           |                             1,300,000 |                         109.14 |                                 68.26 |
| *Galactica BS-75*                | *Battlestar Galactica*                        |                             1,680,000 |                         118.88 |                                 73.72 |
| *Axiom*                          | *Wall-E*                                      |                             2,190,000 |                         129.86 |                                 79.82 |
| Imperial II-Class Star Destroyer | *Star Wars<br>(various)*                      |                             2,285,000 |                         131.71 |                                 80.85 |
| Trimaxion Drone Ship             | *Flight of the Navigator*                     |                             4,460,000 |                         164.61 |                                 98.81 |
| Samus Gunship                    | *Metroid*                                     |                             6,500,000 |                         186.63 |                                110.63 |
| *Millenium Falcon*               | *Star Wars<br>(various)*                      |                             9,130,000 |                         209.01 |                                122.50 |
| Bes'Uliik Starfighter            | *Star Wars<br>(various)*                      |                            11,412,500 |                         225.14 |                                130.98 |
| *Daedalus*                       | *Stargate SG-1*                               |                            60,875,000 |                         393.38 |                                216.44 |
| The *Milano*                     | *Guardians of the Galaxy*                     |                         5,775,040,800 |                        1794.12 |                                848.14 |
These were gathered from a plethora of sources around the internet.  I'm certain there will be disagreements about them; I've only included them for illustration purposes, not to reflect any kind of "canon".

To convert a ship's speed in multiples of the speed of light to a _Star Trek_ warp factor:
$$
f_{TOS} = \sqrt[3]{v} \qquad f_{TNG} = \sqrt[\frac{10}{3}]{v}
$$
For example the _Orville_, taking 10 light years per hour as the standard, would have a "c-speed" of:
$$
\begin{align}
&\frac{10 \text{ly}}{hour} \times 8766\;\text{hours per year} = 
\end{align}
$$
So it's equivalent warp factors would be:
$$
\begin{align}
f_{TOS} &= \sqrt[3]{87660} = \mathbf{44.42} \\
f_{TNG} &= \sqrt[\frac{10}{3}]{87660} = \mathbf{30.4}
\end{align}
$$
## The Devil's In The Details
There were (frequent) inconsistencies in _ST:TOS_.  For instance, in the episode "By Any Other Name" (2/23/1968), the Kelvan commander, Rojan, states that the _Enterprise_ engines would be modified to allow travel to the Andromeda Galaxy in 300 Earth-years, and that the ship's cruising speed would thus be warp 11.

However, Andromeda is 2.5 million lightyears away.  Making the journey in 300 years would mean a velocity of:
$$
v = \frac{2500000}{300} = 8333.33\tfrac{ly}{y}
$$
… which equates to a TOS warp factor of:
$$
f_{TOS} = \sqrt[3]{8333.33} = \mathbf{20.274}
$$
… which is 184.3% of warp 11.

The *actual velocity* at warp 11 is:
$$
v = 11^3 = 1331c
$$
… which would mean the trip would take:
$$
v = \frac{2500000}{1331} = \mathbf{1878.287}\;\textbf{years}
$$
This is a prime teaching example for WCB: either a) the writers did not have an accurate distance value for Andromeda; b) they did their math wrong; c) they didn't bother with the math and wrote dialogue that sounded cool.

# Forbidden Planet
Perhaps ironically, one of the most accurate-seeming depictions of an FTL drive comes from one of the earliest: _Forbidden Planet_ (1956).  The ship, United Planets _C57D_, was said to use a "hyper-drive".  I cannot find any specific numbers for its top velocity, but some clues in the narrative and dialogue are available.  The opening voice-over says that the ship was "… more than a year out from Earth base." on a mission to Altair IV, the fourth planet of the star, Altair (α Aquilae).  Later, Commander Adams exasperatedly explains to Altaira Morbius that she needs to wear less revealing outfits because is crew has been "… locked up in hyperspace for 378 days," which is 1.035 years.

The modern distance to Altair from Earth is measured at 16.73 light-years.  From this, we can calculate that the _C57D_ traveled:
$$
v = \frac{D}{T} = \frac{16.73}{1.035} ≈ 16.164\;\text{ligh-years per year} 
$$
It seems reasonable to suppose that the _intended_ velocity was meant to be a nice, round $16$ lightyears per year, which would indicate that the writers used:
$$
D = v \times T = 16 \times 1.035 = 16.56\;\text{light-years}
$$
as the distance to Altair.  A velocity of $16$ light-years per year equates to a ST:TOS warp factor of:
$$
f = \sqrt[3]{v} = \sqrt[3]{16} = 2.52
$$
This seems like an unusually rigorous early attempt to quantify FTL, unlike later franchises that often hand-waved the numbers. More likely, though, it was a lucky coincidence: the narrative hook of a long, lonely voyage (378 days) paired with the choice of Altair — a star whose name conveniently provided an exotic but pronounceable basis for the female lead, Altaira. Had Irving Block and Allen Adler (story) or Cyril Hume (screenplay) been consciously designing a hyperdrive system, it would make more sense for them to have chosen a clean round figure like 15 light-years per year or 20 light-years per year, in the same vein as *The Orville*’s “ten light-years per hour.”

This is not to dismiss the breadth and creativity of the writers’ efforts. Rather, it highlights how “the math” of a milieu can often be back-calculated from clues in dialogue or values glimpsed on a display, even when the creators themselves were (rightly) more focused on metaphor than mathematics.

Miguel Alcubierre floated the idea in 1994 of a real-world warp drive as a scientific possibility, and we’d be remiss not to visit his theory here.

Einstein’s general relativity shows that a physical object is limited to the speed of light _within_ spacetime, but spacetime itself can expand, contract, or move without such restrictions. Alcubierre hypothesized a system where space behind a ship is compressed (a “wave crest”) and space ahead is rarified (a “trough”), creating an energetic slope along which the ship rides — much like a surfer gliding on a wave.

The analogy is apt: ocean waves don’t carry the water itself forward, they make it undulate. A cork or buoy bobs in place while the wave passes beneath. In the warp drive concept, the ship never moves through local spacetime; instead, spacetime itself is carried forward with the vessel inside.

Alcubierre’s first model required infinite “negative energy,” but later refinements reduced the demand to merely astronomical levels — the mass-energy of planets or stars, still far beyond our reach. The concept remains speculative, and even potentially hazardous: some physicists suggest that halting the bubble would release catastrophic radiation, tearing apart the ship in a man-made supernova.

Still, the idea is tantalizing. Even a conservative Alcubierre drive running at 10c (≈ warp 2.15, TOS; ≈ warp 2.0, TNG) would put Alpha Centauri a little over five months from Earth. Within the Solar System, 0.1c would place Mars just hours away — a vast improvement over the year-long, radiation-bathed voyages chemical rockets imply.

Crucially, crew inside a warp bubble would experience **no relativistic time dilation**: their five-month trip would feel like five months. Like the crew of the _C57D_ in _Forbidden Planet_, they’d still have to occupy themselves en route, but they wouldn’t return home displaced from their origin time by months, decades, or even centuries, depending on the distance traveled.

For comparison, a ship traveling at 0.99c would take about **2626 years** to reach Deneb as measured from Earth, while only **367 years** would pass onboard — still a generation ship, but 18 generations instead of 131. By contrast, an Alcubierre drive at 10c would reach Deneb in just **260 years**, with both ship and Earth clocks agreeing on the elapsed time — the same 13 generations would pass in both frames.

A fascinating sidelight, though, is that even if the _ship_ arrives in only 260 years, its _“we have arrived!”_ signal — still limited to lightspeed — would take **2600 years** to reach Earth. Ironically, if the explorers also dispatched a ship back home, it would return in **260 years**, arriving a full **2340 years before** the radio message did!

This is a prime example of **world*crafting*** meeting **world*building***: the numbers are what they are, but the drama lies in how people adapt to — and live with — those inescapable realities.

Warp drives, hyperdrives, subspace drives, quantum drives, etc., all share the common basic notion of *actual, physical travel* through spacetime (or some subrealm thereof).  Even the Alcubierre metric assumes forward "motion" within a "bubble" of "normal" spacetime.

Other creators have opted for different solutions to the time-distance dilemma.

## Space Folding and Jump Drives
### Space Folding
Perhaps the best-known example of “space-folding” comes from Frank Herbert’s _Dune_ universe. Spacing Guild Navigators, their mental faculties expanded by the spice _melange_, cause two distant points in space to momentarily overlap, like bending a sheet of paper so that a point 1" from each opposing margin are brought into contact.  At that moment, a ship could physically relocate from origin to destination without traversing the intervening void (which, for that moment, would not actually exist). When space “unfolds,” the ship is simply _there_. For all practical purposes, the voyage is instantaneous — it takes longer to ride the shuttle up to orbit at origin and back down at destination than it does to cross between worlds.

This, of course, is entirely speculative (or outright fantastical), and even if realizable, would demand at least **Kardashev Type IV** technologies — the ability to manipulate energy on galactic scales. Yet from a world*building* perspective, _instant travel_ shifts the storytelling focus: the challenge is no longer the journey, but who controls the technology/mechanology of travel and transportation.
### Jump Drives
Jump drives accomplish much the same function as space-folding, but by **mechanotechnological (mechtech)** means rather than mystical or mental ones. The “FTL jumps” of _Battlestar Galactica_ (both versions) are a classic example, as is the “blink drive” in _Dark Matter_.

Depending on the needs of the setting, a jump drive may require measurable amounts of time and energy, or it may be treated as effectively instantaneous — “supertech” that simply relocates a ship. Likewise, jumps may be chained one after another, or require a recharge interval before firing again.

From a world*building* standpoint, these choices are critical: do you want drama from fuel shortages, from cooldown tension, from misjumps into the void — or from the sheer ease of hopping anywhere instantly? The math is malleable, but the **drama comes from the limits you set.**

This is why such mechtech is often preferred by more speculative writers: you don’t have to wrestle with the intractable realities of hard science. Instead, the _means_ recedes into the background, letting the drama occupy the foreground — focusing on the characters and their story.
### Practicum
With space-folding and jumpdrives, etc., instead of determining a maximum velocity in terms of lightspeed, one might specify a maximum traversable distance per jump, limited by available drive power, fuel consumption, or whatever other constraint one may choose to impose.

For instance, let's posit an interstellar civilization, the Serelem Union which has developed a "vault drive" with the parameters:
- Individual vaults can span any distance between 1 and 100 light-years
- The more extensive the vault, the more energy required
- The more extensive the vault, the longer the drive takes to recharge, such that
	- The vault-to-charge ratio is 1 minute of recharge per light-year of the most recent previous vault.

Now let posit the Serelemene flagship, _Tonqua_, is on a defense/rescue mission to their most distant outpost on a planet called Rylboru, $4835$ lightyears from the homeworld.  How long does it take _Tonqua_ to get there (we'll be using Earth-normal time units here for convenience)?

The number of vaults required depends on the chosen vault magnitude.  At one light-year per vault, it is $4835$ vaults; at 100 light-years per vault it is $48.35$ vaults (or, more likely $48$ vaults of $100$ light-years and a final vault of $35$ light-years.).  Let's say Captain Talua decides to make $100$ light-year vaults.  That means that after each vault, the _Tonqua_ will have to spend 100 minutes recharging its drive before it can vault again.
$$
\begin{align}
T &= 48\;\text{vaults} \times 100\;\text{minutes} = 4800\;\text{minutes} \\[0.5em]
&= \frac{4800\;\text{minutes}}{60\;\text{minutes/hour}} = 80\;\text{hours} \\[0.5em]
&= \frac{80\;\text{hours}}{24\;\text{hr/day}} = 3.\overline{3}\;\text{days} \\[0.5em]
&≈ 3\;\text{days, } 8\;\text{hours}
\end{align}
$$
(We don't need to account for the recharge time after the last $35$ light-year vault, because it will transpire at the destination.)

This equates to an apparent velocity of:
$$
\begin{align}
v &= \frac{D}{T} = \frac{4800}{3.\overline{3}} = 1440\;\text{light-years per day} \\[0.5em]
&\text{Remember that the last vault adds recharge time, but not travel time!} \\[0.5em]
&= 1440\;\text{ly/day} \times 365.25\;\text{days} \\[0.5em]
&= 525960\;\text{light-years per year} \\[0.5em]
&= 525960c \\[1.5em]
f_{TOS} &= \sqrt[\frac{10}{3}]{525960} = 80.721
\end{align}
$$
To put it another way, a _ST:TOS_ ship at warp $8$ would need $9.44$ days to cover the same distance.

> Note that the travel time is the same regardless of how the vaults are chosen, arranged.
> - $1000$ vaults of 1 minute recharge each is still a total of $4800$ minutes of recharge
> - $100$ vaults of $24$ light-years means $2400$ minutes of recharge; completing the trip with $2400$ vaults of 1 light-year is another $2400$ minutes of recharge, for, again, a total of $4800$ minutes of recharge.

Looking back at our ship speed listing from earlier this makes _Tonqua_
- About $\frac{1}{17}$ times as fast as the _Millennium Falcon_
- Approximately $\frac{3}{4}$ as fast as the _GunStar_
- Around $1.44$ times faster than the _Moya_
- _Exactly_ $6$ times faster than the  _Orville_
- More-or-less $548.45$ times faster than the _PIllar of Autumn_
- *Precisely* $2435$ times faster than *ST:TOS* warp 6
### Wormholes and Stargates

Travel by wormhole, as in _Star Trek: Deep Space Nine_ or _Stargate_, achieves the same end as space-folding or jump drives, but by exploiting a hypothesized natural phenomenon: conduits in spacetime that connect two distant points through a substrate (or superstrate) of “normal” space.

Naturally occurring wormholes may have permanently fixed endpoints: you enter one end of the Chunnel and you always exit the other. Or they may be unstable: opening and closing at unpredictable intervals; fixed at one end but wandering at the other; or even distorting time so that traversal involves dilation — or outright _time travel_.

> Imagine a milieu in which an advanced civilization builds a galaxy-spanning civilization by means of a wormhole, unaware that one end of the conduit is temporally displaced by millennia. If physical travel between the two termini is impossible, would the discrepancy in eras even _matter_?

Another dramatic limitation, as in _Stargate_, is when wormholes are generated by **mechtech** devices. In that case, both origin and destination must host a physical machine — which can itself be relocated, creating the possibility of shifting or contesting endpoints.

As always, one may specify instantaneous or finite-time traversal, and decide how such wormholes are powered. The physics can be left hand-wavy — what matters for world_building_ is how these limits shape drama, conflict, and control.

The worldmaker will be confronted with a decision in designing interstellar polities. You either:
1. Invent your space-traversing technology, determine its limitations, and design the volumetric span of your civilization based on the longest necessary travel-time; or,
2. Create your milieu, including the size of your civilization's sphere of influence, and then design a drive that lets your characters get around that volume of space in reasonable amounts of time.

## Example: The Kaltai Entente
Let's specify a moderately sized elliptical galaxy (Shuf) of $10$ billion stars, spanning $350000$ light-years.  The Kaltai Entente is a federated polity of cooperative star systems that extends $1500$ light-years in radius out from the central star (Kaltai).  Thus, the Entente commands a spherical volume of about $14$ billion cubic light-years, encompassing $56.5$ _million_ star systems of which about $13$ _million_ are habitable/hospitable systems around F-, G-, and K-type stars.  That's a lot of space (and stars, and planets) to watch over.

Let's further say that the military-supported trade syndicate (KaltaiSys) has a monopoly on the modes of FTL space travel, and that there are no space-folding drive, or jump drives, or wormhole, etc.  All travel is inherently time-consumptive, distance-over-rate.  Their fastest battle cruisers can make the trip between Kaltai and their most distant colony at Taibano Raimos, 1500 light-years away, in 10 days.

Thus, these ships are capable of:
$$
\begin{align}
r &= \frac{1500\;\text{light years}}{10\;\text{days}} = 150\;\text{ly/day} \\[0.5em]
v &= 150\;\text{ly/day} \times 365.25\;\text{days/yr} = 54787.5\;\text{light-years/yr} \\[0.5em]
&= 54787.5c
\end{align}
$$
This equates to:
- _ST:TOS_ warp $37.9$
- About $12.5$% faster that a Wraith hive ship in _Stargate: Atlantis_; and
- $62.5$% of the top speed of the _Orville_

If your game, story, or show can tolerate a **10-day lag** between core and frontier, then this drive system fits your setting. But if you need supplies, reinforcements, or diplomacy to move faster than that — and you don’t want to shrink your sphere of influence — you have only two real options: 
- **Reconfigure your FTL.** Make the drive faster, reduce recharge, or relax the limits you’ve set.  
- **Invent another traversal process.** Wormholes, jump drives, fold engines, or some other mechanism that bypasses the distance–rate bottleneck altogether.

The Lorentz term is a factor of how much the local passage of time, length (in the direction of motion), and relativistic mass change when an object is in motion.
$$
\gamma = \frac{1}{\sqrt{1-\beta^2}}
$$
Where:
- $\beta$ = the velocity expressed as a percentage of the speed of light $^v/_c$.

All motion results in some magnitude of the Lorentz term (GPS satellites have to take it into account to return accurate results).  As velocity increases, the Lorentz term increases exponentially.

This equation was developed by the Dutch Physicist Hendrik Lorentz in the late $19^{th}$ century as part of a broader set of equations called the Lorentz transformations.  He developed these as part of his effort to determine whether or not a cosmic space-filling substance (_luminous æther_) existed.  (It doesn't).

When it became clear that all electromagnetic phenomena, including visible light, has wavelike properties, it was believed that all waves needed a physical medium through which to propagate.  It was reasoned, then, that there must be a substance filling "empty" space in which light waves moved.  Yet all attempts to detect or measure the qualities of this æther failed.

An early explanation of the failure of these experiments was that linear distances might be compressed in the direction of motion due to pressure from the æther building up against the forward faces of the object.  If this were true, then light waves and any measuring device would also be compressed along the same vector and so a measurment would always return the same value because all elements of the system were being altered by the same ratio.

Lorentz developed his equations to calculate the amount of compression that motion through the æther would cause. When Michelson and Morley’s experiments showed that the æther did not exist — and did not need to — the math itself did not vanish. Lorentz had the equations right, but the _context_ wrong. A generation later, Einstein reinterpreted them: not as distortions caused by a cosmic medium, but as the natural geometry of spacetime itself.

Einstein's recontextualizing of the Lorentz transformations shows that, as the velocity of an object such as a space ship approaches the speed of light, the ship's linear dimension in the direction of motion contracts — so that much of the theory **was** true, there just wasn't any substance physically causing the contraction.

Einstein also realized that for the object in motion, time passes more slowly by the same Lorentz factor (though to an observer on or in the moving object, no change in the "flow" of time is apparent).  And, finally, the kinetic mass of the ship (as measured by an outside observer), also increases by the same factor of the Lorentz term.  Thus, the speed of light, the passage of time, and mass are all constant for every observer.  A passenger onboard a ship with a velocity of 0.99c would measure a rod as a meter long, while to an outside observer, the rod would appear shorter by the factor:
$$
\frac{1}{\gamma} = \sqrt{1 - 0.99^2} = \sqrt{1 - 0.98} = \sqrt{0.0199} = 0.1411
$$
To the outside observer, the rod would appear to be only about $14.1$ cm in length.

> Note: this shows that while length _contracts_, time _expands_ and mass _increases_.  To calculate
> - Length contraction: multiply by $\frac{1}{\gamma}$
> - Time dilation (expansion): multiply by $\gamma$.
> - Mass increase: multiply by $\gamma$.

For example: to those inside the ship, one minute would be sixty seconds long.  To those looking in from outside, a minute on the ship would last:
$$
\begin{align}
\gamma &= \frac{1}{\sqrt{1 - 0.99^2}} = \frac{1}{\sqrt{1 - 0.98}} = \frac{1}{\sqrt{0.0199}} = \frac{1}{0.1411} = 7.089 \\[0.5em]
T_\gamma &= 60 \times 7.089 ≈ 425\;\text{seconds}
\end{align}
$$
… just over 425 seconds — or 7.089 minutes (7ᵐ 5.33ˢ).

A $50$-kilogram person stepping on a scale onboard ship would see the scale report their weight as $50$ kilograms, but if an exterior observer were able to measure the person's mass, they would see them weighing almost $355$ kilograms.  Also, if the person onboard the ship made a round trip of $50$ years according to their clock, they would return to find that almost $355$ years had passed on Earth!

> This is the source of the so-called "Twin Paradox": if one twin makes a round-trip journey at $0.99$c of $10$ years by their own clock, they will return to find that about $71$ years have passed on Earth. If both twins were both $20$ years old at departure, the traveler will return at age $30$ — to a sibling who has aged through all of those $71$ years and is now $91$ years old, making the stay-at-home twin **$\mathbf{61}$ years older** than their traveling sibling.

This shows that at rest (in one's own reference frame) the Lorentz term is 1.0, but as soon as _any_ motion is applied, a Lorentz term comes into effect — small at first but growing rapidly as the velocity approaches the speed of light.  At 0.9999c, the Lorentz term is:
$$
\gamma = \frac{1}{\sqrt{1 - 0.9999^2}} = \frac{1}{\sqrt{1 - 0.9998}} = \frac{1}{\sqrt{0.0000199}} = \frac{1}{0.01411} = 70.7
$$
**Table of Lorentz Factors**

| <center>Fraction of<br>lightspeed</center> | <center>Lorentz factor<br>(γ)</center> |
| ---------------------------------------------: | -----------------------------------------: |
|                                            0.9 |                                2.294157339 |
|                                           0.99 |                                 7.08881205 |
|                                          0.999 |                                22.36627204 |
|                                         0.9999 |                                70.71244595 |
|                                        0.99999 |                                223.6073568 |
|                                       0.999999 |                                707.1069579 |
|                                      0.9999999 |                                2236.068034 |
|                                     0.99999999 |                                7071.067814 |
|                                    0.999999999 |                                22360.68009 |
This is the source of the common expression "nothing can travel faster than light"; at the speed of light it would require an infinite amount of energy to increase velocity by the minuscule amount needed to "break the light barrier".
## The Dramatic Side of Relativity
One of the "features" of relativity is that there is no "correct" frame of reference.  We've noted above that the crew of a ship traversing at 0.99c still measures a minute as 60 seconds, whereas to "back home" that "minute" lasts 7 minutes and 5.33 seconds.

At velocities even closer to the speed of light, the dilation becomes even more pronounced.  You might only experience 10 biological years aboard ship (assuming you don't spend most of the trip in cryostasis), but the "wider universe" may experience tens of thousands of chronological years.  It might happen that "back home" invents a warp drive 10 years into your journey and you arrive at your destination to find that it was colonized and tamed 9500 years ago and nobody actually remembers who you are.

The concept of "age" would necessarily take on new meaning.  Let's revisit the 0.99c scenario and make you the traveling twin.

Assuming cryostasis slows your aging down to 1 year out of every 10 years of ship-time, you'll have only biologically aged a year on your journey, so your "bioage" (let's keep the word "age" to refer to this) is only 21.  Your "proper age" is 11 years more than that (let's call that your "scope"); and the chronological duration since you were born is 71 years (we'll call that your "span")... So you are 21 years of age; 30 years "scoped", and 91 years "spanned".

A $1 you left in a high-yield savings account before your departure may have appreciated into billions — or your culture may have completely changed its material wealth concept and you have no wealth at all under the new system.  Perhaps you carried a million dollars worth of diamonds with you on your journey, but "back home" found and began mining a diamond planet 7 years after you left and now that compressed carbon in your pocket is literally more common than dirt.... 

The world*building* opportunities are endless, and endlessly fascinating.

# The Dangers of Relativistic Velocities
## Catastrophic Impacts From Microparticles
While your environment onboard ship feels "normal" to you, the Lorentz factor has had its effects on the "outside" universe.  A dust particle that would be practically massless under "normal" circumstances may have several tons of relativistic mass if it hits your ship.

So, any vessel traversing at relativistic speeds needs to be protected from the energy release of any such impacts on its hull.  The necessary thickness (and mass that has to be accelerated) of a physical shield grows as a function of the Lorentz factor as velocity increases, so a point of diminishing returns is reached almost instantly.

In many science fiction milieux, this problem is avoided by either of two means:
1. Either the ship is in a "bubble" of some kind, the nature of which absorbs or deflects any such incoming missles; or
2. The ship is fitted with some kind of energetic field of force (commonly called a "shield") which either deflects the impactors or absorbs the energy of their collision with it.

## The View Out The Window
First, it would depend entirely on which window you were looking out of.

1. Light from the stars behind you would become progressively more redshifted as your velocity increased, until they became invisible to the naked eye.  Objects previously radiating in the ultraviolet would gradually become visible and grow redder until they, too, passed beyond the visible red end of the spectrum.
2. Light from the stars ahead of you would become progressively more blue-shifted toward the ultraviolet.  Those already radiating in the violet end of the spectrum would disappear from view.  Objects previously only radiating in long wavelengths below red would emerge into the visible spectrum, progressively grow bluer, and finally, they, too would pass out of the visible range into the ultraviolet.  The light coming toward you would also become progressively more and more energetic until it was as if you were stationary at some finite distance from the Big Bang, itself.
3. Light from the stars out the side windows would be similarly shifted, to a greater or lesser extent depending on how far away from you they were.  Ultimately, all the light arriving at your location would become compressed into a rainbow like a belt around your ship (at no measurable distance_, with utter blackness "ahead" and "behind" it.  Red would be at the "back" end, violet at the "front" end, and the other colors of the spectrum distributed between the two extremes.

And you probably wouldn't want to be looking out a glass window, anyway, because you'd be microwaved or gamma rayed before you had a chance to marvel at the spectacle.