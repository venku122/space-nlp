
import spacy
import textacy.extract
import textacy.keyterms

# Load the large English NLP model
nlp = spacy.load('en_core_web_lg')

# The text we want to examine
text = """"
 
Home - Search - Browse - Alphabetic Index: 0- 1- 2- 3- 4- 5- 6- 7- 8- 9
A- B- C- D- E- F- G- H- I- J- K- L- M- N- O- P- Q- R- S- T- U- V- W- X- Y- Z
Saturn V
Saturn V Geneology

Saturn V Geneology
Credit: © Mark Wade
American orbital launch vehicle. America's booster for the Apollo manned lunar landing. The design was frozen before a landing mode was selected; the Saturn V could be used for either Earth-Orbit-Rendezvous or Lunar-Orbit-Rendezvous methods. The vehicle ended up with the same payload capability as the 'too large' Nova. The basic diameter was dictated by the ceiling height at the Michoud factory selected for first stage manufacture. Despite the study of innumerable variants, production was ended after only 12 were built and America spent the next fifty years in a pointless slow-motion withdrawal from manned space exploration.
AKA: SaturnV. Status: Retired 1973. First Launch: 1967-11-09. Last Launch: 1973-05-14. Number: 13 . Payload: 118,000 kg (260,000 lb). Thrust: 33,737.90 kN (7,584,582 lbf). Gross mass: 3,038,500 kg (6,698,700 lb). Height: 102.00 m (334.00 ft). Diameter: 10.06 m (33.00 ft). Apogee: 185 km (114 mi).

The Saturn launch vehicle was the penultimate expression of the Peenemuende Rocket Team's designs for manned exploration of the moon and Mars. The designs were continuously developed and improved, starting from the World War II A11 and A12 satellite and manned shuttle launcher, through the designs made public in the Collier's Magazine series of the early 1950's, until the shock of the first Sputnik launch brought sudden real interest from the U.S. government. On December 30 1957 Von Braun produced a 'Proposal for a National Integrated Missile and Space Vehicle Development Plan'. This had the first mention of a 1,500,000 lbf booster (Juno V, later Saturn I). By July of the following year Huntsville had in hand the contract from ARPA to proceed with design of the Juno V.

Following transfer of the Peenemuende Rocket Team from the US Army to NASA, a year after the first plan was mooted, Von Braun briefed NASA on plans for booster development at Huntsville with objective of manned lunar landing. It was initially proposed that 15 Juno V (Saturn I) boosters assemble a 200,000 kg payload in earth orbit for direct landing on moon. NASA produced two months later, on February 15, 1959, its plan for development in the next decade of Vega (later cancelled after NASA discovered the USAF was secretly developing the similar Hustler (Agena) upper stage), Centaur, Saturn, and Nova launch vehicles (Juno V renamed Saturn I at this point). Throughout the initial planning, Presidential decision, and landing mode debate for the Apollo lunar landing goal, a variety of Saturn and Nova configurations were considered. Of these, only the C-1 and C-5 were taken through to further development.

Configuration	Stage 1	Stage 2	Stage 3	Stage 4	LEO Payload - kg	Escape Payload - kg
Saturn A-1	8 x H-1	2 x LR89	2 x LR115			
Saturn A-2	8 x H-1	4 x S-3	2 x LR115			
Saturn B-1	8 x H-1	4 x LR89	5 x LR115	2 x LR115		
Saturn C-1	8 x H-1	6 x LR115	2 x LR115		9,000	2,200
Saturn C-2	8 x H-1	1 x J-2	6 x LR115	2 x LR115	20,000	6,800
Saturn C-3	2 x F-1	4 x J-2	6 x LR115	2 x LR115		
Saturn C-4	4 x F-1	4 x J-2	1 x J-2			
Saturn C-5	5 x F-1	5 x J-2	1 x J-2		127,000	45,000
Nova Basic	6 x F-1	1 x F-1	4 x J-2		68,000	16,000
Nova A	4 x F-1	4 x J-2	5 x LR115	1 x 2700 kgf	68,000	27,000
Nova B	6 x F-1	8 x J-2	7 x LR115	1 x LR115	112,000	47,000
Nova C	6 x F-1	8 x J-2	1 x Nerva		68,000	38,000
Nova D	6 x F-1	8 x J-2	1 x Nerva		112,000	65,000
Nova N-F1	8 x F-1	4 x F-1	1 x J-2			70,000
Nova N-M1	8 x F-1	4 x M-1	1 x J-2		180,000	90,000

After the Saturn V drawings had been issued, Marshall engineers immediately turned to considering further developments of the basic launch vehicle. These would be required for Apollo Applications, Manned Orbiting Research Laboratory, Mars fly-by, and Mars landing missions in the 1970's and 1980's.

Contracts were let for a variety of trade studies. There were limits to how far the core stack could be stretched, dictated by the 410 foot maximum overhead crane height in the Vertical Assembly Building at Kennedy Space Center (this did not prevent 470 foot versions being proposed, including the nuclear NERVA third stage, for manned missions to Mars - they'd just have to raise the roof, darn it). Given these limits, a variety of strap-on solid motors were considered.

The most feasible, lowest development cost improvement would have used upgraded F-1 motors, an S- IC first stage stretch, modest upgrades to the J-2 upper stage motors, and proven 120 inch solid rocket motor strap-ons. If a follow-on Saturn V production contract had ever been issued, it probably would have been for this configuration. More advanced versions would have used Flox oxidizer (liquid fluorine mixed with the liquid oxygen oxidizer - nasty to handle, but increased performance with minimal changes to the existing motors and pumps), new technology engines (plug nozzles or high-pressure combustion engines - the ancestors of the Shuttle SSME's). Instead America abandoned its heavy lift capability and further manned exploration of space. The two unused flightworthy Saturn V's from the initial production run of 15 became tourist displays at Cape Canaveral and Huntsville. A third Saturn V, exhibited in Houston, is made up of static test article stages.

Saturn II First Stage Derivatives

There was a large payload gap between the Saturn IB's 19,000 kg low-earth orbit capacity and the two-stage Saturn V's 100,000 kg capability. Marshall considered the best way to fill the gap was to use the Saturn V's second stage, the S-II, as the first stage of an intermediate launch vehicle.

Using the S-II had several advantages. It could be mounted atop a 'milk stool' and use the existing Saturn V launch gantry arms and plumbing for fueling and preparations (this approach was actually used later for Saturn IB launches for Skylab and ASTP). Discontinuing use of the Saturn IB would eliminate one rocket stage production line together with associated configuration and quality control headaches.

A dazzling array of combinations of S-II stages, S-IVB stages, and a variety of solid rocket motor strapons were considered. In most cases the S-II would have to be fitted with 'sea-level' versions of its J-2 engines, which were designed only for operation in near-vacuum conditions. This resulted in a decrease in engine performance. Since the S-II stage did not have enough thrust to get off the ground by itself, various combinations of solid rocket motor augmentation and propellant off-loads had to be used. The resulting configurations would have provided a payload range of between 13,000 kg and 66,000 kg to low earth orbit, thereby filling the payload gap and replacing the S-IB.

LEO Payload: 118,000 kg (260,000 lb) to a 185 km orbit at 28.00 degrees. Payload: 47,000 kg (103,000 lb) to a translunar trajectory. Development Cost $: 7,439.600 million. Launch Price $: 431.000 million in 1967 dollars in 1966 dollars.

Stage Data - Saturn V

Stage 1. 1 x Saturn IC. Gross Mass: 2,286,217 kg (5,040,245 lb). Empty Mass: 135,218 kg (298,104 lb). Thrust (vac): 38,703.160 kN (8,700,816 lbf). Isp: 304 sec. Burn time: 161 sec. Isp(sl): 265 sec. Diameter: 10.06 m (33.00 ft). Span: 19.00 m (62.00 ft). Length: 42.06 m (137.99 ft). Propellants: Lox/Kerosene. No Engines: 5. Engine: F-1. Status: Out of Production.
Stage 2. 1 x Saturn II. Gross Mass: 490,778 kg (1,081,980 lb). Empty Mass: 39,048 kg (86,086 lb). Thrust (vac): 5,165.790 kN (1,161,316 lbf). Isp: 421 sec. Burn time: 390 sec. Isp(sl): 200 sec. Diameter: 10.06 m (33.00 ft). Span: 10.06 m (33.00 ft). Length: 24.84 m (81.49 ft). Propellants: Lox/LH2. No Engines: 5. Engine: J-2. Status: Out of Production.
Stage 3. 1 x Saturn IVB (S-V). Gross Mass: 119,900 kg (264,300 lb). Empty Mass: 13,300 kg (29,300 lb). Thrust (vac): 1,031.600 kN (231,913 lbf). Isp: 421 sec. Burn time: 475 sec. Isp(sl): 200 sec. Diameter: 6.61 m (21.68 ft). Span: 6.61 m (21.68 ft). Length: 17.80 m (58.30 ft). Propellants: Lox/LH2. No Engines: 1. Engine: J-2. Status: Out of Production. Comments: Saturn V version of S-IVB stage.
More at: Saturn V.
Subtopics
	Saturn C-3 The launch vehicle concept considered for a time as the leading contender for the Earth Orbit Rendezvous approach to an American lunar landing.
	Saturn C-3B American orbital launch vehicle. Final configuration of the Saturn C-3 at the time of selection of the Saturn C-5 configuration for the Apollo program in December 1961.
	Saturn C-3BN American nuclear orbital launch vehicle. Version of Saturn C-3 considered with small nuclear thermal stage in place of S-IVB oxygen/hydrogen stage.
	Saturn C-4 American orbital launch vehicle. The launch vehicle actually planned for the Lunar Orbit Rendezvous approach to lunar landing. The Saturn C-5 was selected instead to have reserve capacity.
	Saturn C-4B American orbital launch vehicle. Final configuration of the Saturn C-4 at the time of selection of the Saturn C-5 configuration for the Apollo program in December 1961. Only Saturn configuration with common bulkhead propellant tanks in first stage, resulting in shorter vehicle than less powerful Saturn C-3.
	Saturn C-5 American orbital launch vehicle. Final configuration of Saturn C-5 at the time of selection of this configuration for the Apollo program in December 1961. The actual Saturn V would be derived from this, but with an increased-diameter third stage (6.61 m vs 5.59 m in C-5) and increased propellant load in S-II second stage.
	Saturn C-5N American nuclear orbital launch vehicle. Version of Saturn C-5 considered with small nuclear thermal stage in place of S-IVB oxygen/hydrogen stage.
Winged Saturn V North American's study was dated 18 March 1963. The second alternative was a two-stage reusable booster derived from the Saturn V. This would boost either an 11,400 kg cargo, or a half-disc lifting body spaceplane, which would accommodate two crew plus ten passengers and minor cargo
	Saturn MLV-V-4(S) American orbital launch vehicle. MSFC study, 1965. Saturn V core, strengthened but not stretched, with 4 Titan UA1205 strap-on solid rocket boosters.
	Saturn MLV-V-1 American orbital launch vehicle. MSFC study, 1965. Improved Saturn V configuration studied under contract NAS8-11359. Saturn IC stretched 240 inches with 5.6 million pounds propellant and 5 F-1A engines; S-II stretched 41 inches with 1.0 million pounds propellant and 5 J-2 engines; S-IVB strengthened but with standard 230,000 lbs propellant, 1 J-2 engine.
	Saturn MLV-V-2 American orbital launch vehicle. MSFC study, 1965. Saturn IC stretched 240 inches with 5.6 million pounds propellant and 5 F-1A engines; S-II stretched 41 inches with 1.0 million pounds propellant and 5 J-2 engines; S-IVB stretched 198 inches with 350,000 lbs propellant, 1 HG-3 engine.
	Saturn MLV-V-3 American orbital launch vehicle. MSFC study, 1965. Ultimate core for improved Saturn V configurations studied under contract NAS8-11359. Saturn IC stretched 240 inches with 5.6 million pounds propellant and 5 F-1A engines; S-II stretched 156 inches with 1.2 million pounds propellant and 5 HG-3 engines; S-IVB stretched 198 inches with 350,000 lbs propellant, 1 HG-3 engine.
Saturn MLV-V-1A American orbital launch vehicle. MSFC study, 1965. Saturn IC stretched 240 inches with 5.6 million pounds propellant and 6 F-1 engines; S-II stretched 156 inches with 1.2 million pounds propellant and 7 J-2 engines; S-IVB stretched 198 inches with 350,000 lbs propellant, 1 J-2 engine.
	Saturn MLV-V-4(S)-A American orbital launch vehicle. MSFC study, 1965. 4 Titan UA1205 solid rocket boosters; Saturn IC stretched 337 inches with 6.0 million pounds propellant and 5 F-1 engines; S-II with 970,000 pounds propellant and 5 J-2 engines; S-IVB strengthened but with standard 230,000 lbs propellant, 1 J-2 engine.
Saturn MLV-V-1/J-2T/200K American orbital launch vehicle. MSFC study, 1965. Improved Saturn V configuration studied under contract NAS8-11359. Variant of MLV-V-1 with toroidal J-2T-200K engines replacing standard J-2 engines in upper stages.
Saturn MLV-V-1/J-2T/250K American orbital launch vehicle. MSFC study, 1965. Improved Saturn V configuration studied under contract NAS8-11359. Variant of MLV-V-1 with toroidal J-2T-250K engines replacing standard J-2 engines in upper stages.
	Saturn INT-17 North American study, 1966. Saturn variant with a modified S-II first stage with seven high-performance HG-3 engines; S-IVB second stage. Poor performance and cost-effectiveness and not studied further.
	Saturn INT-18 North American study, 1966. Saturn variant with Titan UA1205 or 1207 motors as boosters, Saturn II stage as core, and Saturn IVB upper stage. Various combinations of numbers of strap-ons, propellant loading of the two core stages, and sea-level versus altitude ignition were studied.
	Saturn INT-19 North American study, 1966. Saturn variant with 4 to 12 Minuteman motors as boosters, Saturn II stage as core, and Saturn IVB upper stage. Saturn II stage would be fitted with lower expansion ratio engines and would ignite at sea level. Various combinations of numbers of strap-ons, propellant loading of the two core stages were studied.
Saturn V-ELV American orbital launch vehicle. NASA study, 1966. No-height-limitation stretched Saturn with Titan UA1207 motors for thrust augmentation.
	Saturn V-23(L) American orbital launch vehicle. Boeing study, 1967. 4 260 inch liquid propellant boosters (each with 2 F-1's!).; Saturn IC stretched 240 inches with 5.6 million pounds propellant and 5 F-1 engines; S-II strengthened but with standard 930,000 pounds propellant and 5 J-2 engines; S-IVB stretched 198 inches with 350,000 lbs propellant, 1 J-2 engine.
Saturn V-24(L) American orbital launch vehicle. Boeing study, 1967. 4 260 inch liquid propellant boosters (each with 2 F-1A).; Saturn IC stretched 336 inches with 6.0 million pounds propellant and 5 F-1A engines; S-II stretched 156 inches with 1.2 million pounds propellant and 5 HG-3 engines; S-IVB stretched 198 inches with 350,000 lbs propellant, 1 HG-3 engine. Not studied in detail since vehicle height of 600 feet with payload exceeded study limit of 410 feet.
	Saturn INT-20 American orbital launch vehicle. Saturn variant consisting of S-IC first stage and S-IVB second stage. Consideration was given to deleting one or more of the F-1 engines in the first stage.
Saturn LCB-Storable-140 American orbital launch vehicle. Boeing Low-Cost Saturn Derivative Study, 1967 (trade study of 260 inch first stages for S-IVB, all delivering 86,000 lb payload to LEO): Low Cost Booster, Single Pressure-fed N2O4/UDMH Propellant engine, HY-140 Steel Hull.
Saturn V/4-260 American orbital launch vehicle. Boeing study, 1967-1968. Use of full length 260 inch solid rocket boosters with stretched Saturn IC stages presented problems, since the top of the motors came about half way up the liquid oxygen tank of the stage, making transmission of loads from the motors to the core vehicle complex and adding a great deal of weight to the S-IC. Boeing's solution was to retain the standard length Saturn IC, with the 260 inch motors ending half way up the S-IC/S-II interstage, but to provide additional propellant for the S-IC by putting propellant tanks above the 260 inch boosters. These would be drained first and jettisoned with the boosters. This added to the plumbing complexity but solved the loads problem.
	Saturn INT-21 American orbital launch vehicle. Saturn variant consisting of S-IC first stage and S-II second stage. This essentially flew once to launch Skylab in 1972, although the IU was located atop the Skylab space station (converted S-IVB stage) rather than atop the S-II as in the INT-21 design.
	Saturn MLV-V-4(S)-B American orbital launch vehicle. Boeing study, 1967. Configuration of improved Saturn 5 with Titan UA1207 120 inch solid rocket boosters. Saturn IC stretched 336 inches with 6.0 million pounds propellant and 5 F-1 engines; Saturn II and Saturn IVB stages strengthened but not stretched. Empty mass of stages increased by 13.9% (S-IC), 8.6% (S-II) and 11.8% (S-IVB). Studied again by Boeing in 1967 as Saturn V-4(S)B.
Saturn S-IC-TLB American orbital launch vehicle. Boeing Low-Cost Saturn Derivative Study, 1967 (trade study of 260 inch first stages for S-IVB, all delivering 86,000 lb payload to LEO): S-IC Technology Liquid Booster: 260 inch liquid booster with 2 x F-1 engines, recoverable/reusable
	Saturn V-25(S)B American orbital launch vehicle. Boeing study, 1967. 4 156 inch solid propellant boosters; Saturn IC stretched 498 inches with 6.64 million pounds propellant and 5 F-1 engines; S-II standard length with 5 J-2 engines; S-IVB stretched 198 inches with 350,000 lbs propellant, 1 J-2 engine.
Saturn V-3B American orbital launch vehicle. Boeing study, 1967. Variation on MSFC 1965 study Saturn MLV-V-3 but with toroidal engines. Saturn IC stretched 240 inches with 5.6 million pounds propellant (but only 4.99 million pounds usable without solid rocket boosters) and 5 F-1A engines; S-II stretched 186 inches with 1.29 million lbs propellant and 5 J-2T-400 engines; S-IVB stretched 198 inches with 350,000 lbs propellant, 1 J-2T-400 engine.
Saturn V-4X(U) American orbital launch vehicle. Boeing study, 1968. Four core vehicles from Saturn V-25(S) study lashed together to obtain million-pound payload using existing hardware. First stage consisted of 4 Saturn IC's stretched 498 inches with 6.64 million pounds propellant and 5 F-1 engines; second stage 4 Saturn II standard length stages with 5 J-2 engines
	Saturn V-A American orbital launch vehicle. MSFC study, 1968. Essentially identical to Saturn INT-20; standard Saturn IC stage together with Saturn IVB second stage, with Centaur third stage for deep space missions.
Saturn V-B American orbital launch vehicle. MSFC study, 1968. Intriguing stage-and-a-half to orbit design using Saturn S-ID stage. The S-ID would be the same length and engines as the standard Saturn IC, but the four outer engines and their boost structure would be jettisoned once 70% of the propellant was consumed, as in the Atlas ICBM. This booster engine assembly would be recovered and reused. The center engine would be gimbaled and serve as a sustainer engine to put the rest of the vehicle and its 50,000 pound payload into orbit. At very minimal cost (36 months lead-time and $ 150 million) the United States could have attained a payload capability and level of reusability similar to that of the space shuttle.
Saturn V-C American orbital launch vehicle. MSFC study, 1968. S-ID stage-and-a-half first stage and Saturn IVB second stage. Centaur available as third stage for deep space missions. 30% performance improvement over Saturn V-A/Saturn INT-20 with standard Saturn IC first stage.
	Saturn V-D American orbital launch vehicle. MSFC study, 1968. Rehashed the Boeing 1967 studies, covering a variety of stage stretches and 120, 156, or 260 inch solid rocket boosters, but with S-ID stage-and-a-half first stage.
	Saturn V-Centaur American orbital launch vehicle. MSFC study, 1968. S-ID stage-and-a-half first stage and Saturn IVB second stage. Centaur available as third stage for deep space missions. 30% performance improvement over Saturn V-A/Saturn INT-20 with standard Saturn IC first stage.
Saturn V-25(S)U American orbital launch vehicle. Boeing study, 1968. 4 156 inch solid propellant boosters; Saturn IC stretched 498 inches with 6.64 million pounds propellant and 5 F-1 engines; S-II standard length with 5 J-2 engines. This vehicle would place Nerva nuclear third stage into low earth orbit, where five such stages would be assembled together with the spacecraft for a manned Mars expedition.
	Jarvis launch vehicle American orbital launch vehicle. Launch vehicle planned for Pacific launch based on Saturn V engines, tooling. Masses, payload estimated.
Family: orbital launch vehicle. People: von Braun. Country: USA. Spacecraft: Apollo Lunar Landing, Mercury, Apollo LM, Apollo CSM, Gemini, Gemini Lunar Lander, Lunar Bus, Apollo ULS, Apollo M-1, Apollo W-1, Apollo D-2, Apollo R-3, Apollo L-2C, Apollo Lenticular, LORL, Apollo LM Shelter, Apollo LM Taxi, CSM Electrical, Self-Deploying Space Station, Apollo LM Truck, Apollo MSS, Gemini - Saturn V, Saturn II Stage Wet Workshop, Voyager 1973, GE Lunar NEP Tug, MORL Mars Flyby, Apollo LMSS, Gemini Lunar Surface Rescue Spacecraft, Apollo LTA, Gemini Lunar Surface Survival Shelter, Gemini LORV, Apollo 120 in Telescope, Apollo LMAL, Apollo LASS, LESA Lunar Base, Space Station 1970, Apollo ALSEP, Apollo LRM, LESA Shelter, Space Base, S-IVB Advanced Station, Skylab Lunar Orbit Station, Apollo LRV, PFS, Skylab, AES Lunar Base, ALSS Lunar Base. Projects: Apollo. Launch Sites: Cape Canaveral, Cape Canaveral LC39A, Cape Canaveral LC39B. Stages: Saturn IC, Saturn II, Saturn IVB (S-IB). Bibliography: 16, 17, 18, 2, 216, 222, 228, 229, 230, 231, 233, 26, 27, 33, 34, 47, 6, 60, 4832, 8601.
Photo Gallery
Saturn V 1	Saturn V 1
Credit: NASA
Saturn V	Saturn V
Credit: © Mark Wade
Saturn II stage	Saturn II stage
Credit: © Mark Wade
J-2	J-2
Credit: © Mark Wade
Launch vehicles	Launch vehicles
Launch vehicles of the world as known in 1980
Credit: © Mark Wade
N1 and Saturn V	N1 and Saturn V
Credit: © Mark Wade
Saturn V	Saturn V
Credit: NASA
Saturn V  LV	Saturn V LV
Credit: © Mark Wade
Saturn V 2	Saturn V 2
Credit: NASA
Saturn V No. b	Saturn V No. b
Credit: NASA
Saturn V No. d	Saturn V No. d
Credit: NASA
Saturn V Title	Saturn V Title
Saturn A-1 to C-5	Saturn A-1 to C-5
Credit: © Mark Wade
Saturn C-4B 2 Stage 	Saturn C-4B 2 Stage 
Saturn C-4B 2 Stage version Nov 1961
Credit: © Mark Wade
Saturn C-4B final	Saturn C-4B final
Saturn C-4B final configuration Nov 1961
Credit: © Mark Wade
Saturn 5 final	Saturn 5 final
Saturn 5 final configuration Nov 1961
Credit: © Mark Wade
Saturn 5 nuclear	Saturn 5 nuclear
Saturn 5 nuclear configuration Nov 1961
Credit: © Mark Wade
Saturn MLV 1.37	Saturn MLV 1.37
Credit: © Mark Wade
Saturn 2-120-4	Saturn 2-120-4
Credit: © Mark Wade
Saturn 2-120-5	Saturn 2-120-5
Credit: © Mark Wade
Saturn MLV 2-120-7	Saturn MLV 2-120-7
Credit: © Mark Wade
Saturn 2 w MM SO	Saturn 2 w MM SO
Credit: © Mark Wade
1953 March - . Launch Vehicle: Saturn V.
Research on 1 million lb thrust engine begun. - . Nation: USA. Program: Apollo. Research on 1-million-pound thrust plus engine begun at Rocketdyne, the feasibility of which was established in March 1955..
1955 March - . Launch Vehicle: Saturn V.
Feasibility of million-pound-thrust liquid-fueled rocket engine established - . Nation: USA. Program: Apollo. The feasibility of a million-pound-thrust liquid-fueled rocket engine established by the Rocketdyne Division of North American Aviation, Inc..
1956 January 10 - . Launch Vehicle: Saturn V.
First test of 400,000+ lb thrust engine. - . Nation: USA. Program: Apollo. First U.S.-built complete liquid-rocket engine having a thrust in excess of 400,000 pounds was fired for the first time at Santa Susana, Calif..
1956 November 1 - . Launch Vehicle: Saturn V.
Million pound thrust test stand activiated. - . Nation: USA. Program: Apollo. Rocket test stand capable of testing engines to 1 million pounds thrust activated at Edwards AFB, which became operational in March 1957..
1958 June 23 - . Launch Vehicle: Saturn V.
Preliminary design begun on F-1 - 1.5 million pounds thrust rocket engine - . Nation: USA. Program: Apollo.
The U.S. Air Force contracted with NAA, Rocketdyne Division, for preliminary design of a single-chamber, kerosene and liquid-oxygen rocket engine capable of 1 to 1.5 million pounds of thrust. During the last week in July, Rocketdyne was awarded the contract to develop this engine, designated the F-1.

1958 August 6 - . Launch Vehicle: Saturn V.
Rocketdyne gets F-1 engine contract. - . Nation: USA. Program: Apollo. Rocketdyne Division of North American announced an Air Force contract for a 1-million-pound thrust engine..
1958 November 1 - . Launch Vehicle: Saturn V.
F-1 engine gets highest priority. - . Nation: USA. Program: Apollo. NASA requested DX priority for 1.5-million-pound-thrust F-1 engine project and Project Mercury..
1958 December 17 - . Launch Vehicle: Saturn V.
Rocketdyne gets contract to develop F-1 engine. - . Nation: USA. Program: Apollo. NASA awarded contract to Rocketdyne of North American to build single-chamber 1.5-million-pound-thrust rocket engine..
1959 January 1 - . Launch Vehicle: Saturn V.
1 million pound engine demonstrated. - . Nation: USA. Program: Apollo. Rocketdyne demonstrated 1-million-pound-thrust liquid-propellant rocket combustion chamber at full power..
1959 March 6 - . Launch Vehicle: Saturn V.
Thrust chamber of the Saturn F-1 engine successfully static-fired - . Nation: USA. Program: Apollo.
The thrust chamber of the F-1 engine was successfully static-fired at the Santa Susana Air Force-Rocketdyne Propulsion Laboratory in California. More than one million pounds of thrust were produced, the greatest amount attained to that time in the United States.

1959 June 25-26 - . Launch Vehicle: Saturn V.
Study and research areas for manned flight to and from the moon - . Nation: USA. Program: Apollo. Spacecraft: Mercury. Members of the Research Steering Committee determined the study and research areas which would require emphasis for manned flight to and from the moon and for intermediate flight steps:. Additional Details: here....
1959 August 1 - . Launch Vehicle: Saturn V.
Static firing of the first Saturn planned for early 1960 - . Nation: USA. Program: Apollo.
The Advanced Research Projects Agency (ARPA) directed the Army Ordnance Missile Command to proceed with the static firing of the first Saturn vehicle, the test booster SA-T, in early calendar year 1960 in accordance with the $70 million program and not to accelerate for a January 1960 firing. ARPA asked to be informed of the scheduled firing date.

1959 November 27 - . Launch Vehicle: Saturn V.
Study group to recommend upper-stage configurations - . Nation: USA. Related Persons: Silverstein. Program: Apollo.
While awaiting the formal transfer of the Saturn program, NASA formed a study group to recommend upper-stage configurations. Membership was to include the DOD Director of Defense Research and Engineering and personnel from NASA, Advanced Research Projects Agency, Army Ballistic Missile Agency, and the Air Force. This group was later known both as the Saturn Vehicle Team and the Silverstein Committee (for Abe Silverstein, Chairman).

1959 December 31 - . Launch Vehicle: Saturn V.
NASA approval of Saturn development program - . Nation: USA. Related Persons: Silverstein, von Braun. Program: Apollo.
NASA accepted the recommendations of the Saturn Vehicle Evaluation Committee Silverstein Committee on the Saturn C-1 configuration and on a long-range Saturn program. A research and development plan of ten vehicles was approved. The C-1 configuration would include the S-1 stage (eight H-1 engines clustered, producing 1.5 million pounds of thrust), the S-IV stage (four engines producing 80,000 pounds of thrust), and the S-V stage two engines producing 40,000 pounds of thrust.

1960 January 14 - . Launch Vehicle: Saturn V.
Super booster program to be accelerated - . Nation: USA. Related Persons: Eisenhower, Glennan, von Braun. Program: Apollo.
President Dwight D. Eisenhower directed NASA Administrator T. Keith Glennan "to make a study, to be completed at the earliest date practicable, of the possible need for additional funds for the balance of FY 1960 and for FY 1961 to accelerate the super booster program for which your agency recently was given technical and management responsibility."

1960 February 15 - . Launch Vehicle: Saturn V.
Lunar Program Based on Saturn Systems - . Nation: USA. Related Persons: von Braun. Program: Apollo. Class: Manned. Type: Manned space station. Spacecraft: Apollo Lunar Landing. Study issued by Huntsville of lunar landing alternatives using Saturn systems. Huntsville transferred from Army to NASA. Vought study on modular approach to lunar landing. Internally NASA decides on lunar landing as next objective after Mercury..
1960 Summer - . Launch Vehicle: Saturn V.
Boilerplate Apollo spacecraft to be used on Saturn C-1 - . Nation: USA. Program: Apollo.
H. Kurt Strass of STG and John H. Disher of NASA Headquarters proposed that boilerplate Apollo spacecraft be used in some of the forthcoming Saturn C-1 hunches. (Boilerplates are research and development vehicles which simulate production spacecraft in size, shape, structure, mass, and center of gravity.) These flight tests would provide needed experience with Apollo systems and utilize the Saturn boosters effectively. Four or five such tests were projected. On October 5, agreement was reached between members of Marshall Space Flight Center and STG on tentative Saturn vehicle assignments and flight plans.

1960 September 10 - . Launch Vehicle: Saturn V.
Contract for development of the Saturn J-2 engine - . Nation: USA. Program: Apollo. A NASA contract for approximately $44 million was signed by Rocketdyne Division of NAA for the development of the J-2 engine..
1960 October 5 - . Launch Vehicle: Saturn V.
Discussion of Saturn and Apollo guidance integration - . Nation: USA. Program: Apollo.
Members of STG visited the Marshall Space Flight Center to discuss possible Saturn and Apollo guidance integration and potential utilization of Apollo onboard propulsion to provide a reserve capability. Agreement was reached on tentative Saturn vehicle assignments on abort study and lunar entry simulation; on the use of the Saturn guidance system; and on future preparations of tentative flight plans for Saturns SA-6, 8, 9, and 10.

1961 February 10 - . Launch Vehicle: Saturn V.
First static test of prototype F-1 thrust chamber - . Nation: USA. Program: Apollo. Rocketdyne Division's first static test of a prototype thrust chamber for the F-1 engine achieved a thrust of 1.550 million pounds in a few seconds at Edwards Air Force Base, Calif..
1961 April 6 - . Launch Vehicle: Saturn V.
1,640 million pounds of thrust achieved in static- firing of the F-1 engine - . Nation: USA. Related Persons: von Braun. Program: Apollo. The Marshall Space Flight Center announced that 1.640 million pounds of thrust was achieved in a static- firing of the F-1 engine thrust chamber at Edwards Air Force Base, Calif. This was a record thrust for a single chamber..
1961 April 12 - . Launch Vehicle: Saturn V.
Seamans established the permanent Saturn Program Requirements Committee - . Nation: USA. Program: Apollo.
NASA Associate Administrator Robert C. Seamans, Jr., established the permanent Saturn Program Requirements Committee. Members were William A. Fleming, Chairman; John L. Sloop, Deputy Chairman; Richard B. Canright; John H. Disher; Eldon W. Hall; A. M. Mayo; and Addison M. Rothrock, all of NASA Headquarters. The Committee would review on a continuing basis the mission planning for the utilization of the Saturn and correlate such planning with the Saturn development and procurement plans.

1961 May - . Launch Vehicle: Saturn V.
Reevaluation of the Saturn C-2 to support circumlunar missions - . Nation: USA. Related Persons: von Braun. Program: Apollo. The Marshall Space Flight Center began reevaluation of the Saturn C-2 configuration capability to support circumlunar missions. Results showed that a Saturn vehicle of even greater performance would be desirable..
1961 June 20 - . LV Family: Saturn V. Launch Vehicle: Saturn C-3.
Donald Heaton had been appointed Chairman of an Ad Hoc Task Group - . Nation: USA. Program: Apollo.
Robert C. Seamans, Jr., NASA Associate Administrator, notified the Directors of Launch Vehicle Program, Space Flight Programs, Advanced Research Programs, and Life Sciences Programs that Donald H. Heaton had been appointed Chairman of an Ad Hoc Task Group. It would establish program plans and supporting resources necessary to accomplish the manned lunar landing mission by the use of rendezvous techniques, using the Saturn C-3 launch vehicle, with a target date of 1967. Guidelines and operating methods were similar to those of the Fleming Committee. Members of the Task Group would be appointed from the Offices of Launch Vehicle Programs, Space Flight Program, Advanced Research Programs, and Life Sciences Programs. The work of the Group (Heaton Committee) would be reviewed weekly. The study was completed during August.

1961 July 7 - . Launch Vehicle: Saturn V.
NASA and DoD to study development of large launch vehicles - . Nation: USA. Program: Apollo.
The NASA Administrator and the Secretary of Defense concluded an agreement to study development of large launch vehicles for the national space program. For this purpose, the DOD-NASA Large Launch Vehicle Planning Group was created, reporting to the Associate Administrator of NASA and to the Assistant Secretary of Defense (Deputy Director of Defense Research and Engineering).

1961 July 11 - . Launch Vehicle: Saturn V.
F-1 engine begins static testing. - . Nation: USA. Related Persons: von Braun. Program: Apollo. NASA announced that a complete F-1 engine had begun a series of static test firings at Edwards Rocket Test Center, Calif..
1961 July 20 - . Launch Vehicle: Saturn V.
Large Launch Vehicle Planning Group - . Nation: USA. Program: Apollo. The Large Launch Vehicle Planning Group, established on July 7, 1961, began its formal existence with seven DOD and seven NASA members and alternates.. Additional Details: here....
1961 August 2 - . Launch Vehicle: Saturn V.
Apollo launch site study begun. - . Nation: USA. Program: Apollo.
NASA headquarters announced that it was making a world-wide study of possible launching sites for Moon vehicles; the size, power, noise, and possible hazards of Saturn-Nova type rockets requiring greater isolation for public safety than presently available.

1961 August 16 - . Launch Vehicle: Saturn V.
First F-1 firing. - . Nation: USA. Program: Apollo. F-1 rocket engine tested in first of firing series of the complete flight system..
1961 August 23 - . Launch Vehicle: Saturn V.
Golovin Committee evaluates three rendezvous methods for manned lunar landing - . Nation: USA. Program: Apollo. Spacecraft: Apollo LM, LM ECS, LM Source Selection.
The Large Launch Vehicle Planning Group (Golovin Committee) notified the Marshal! Space Flight Center (MSFC), Langley Research Center, and the Jet Propulsion Laboratory (JPL) that the Group was planning to undertake a comparative evaluation of three types of rendezvous operations and direct flight for manned lunar landing. Rendezvous methods were earth orbit, lunar orbit, and lunar surface. MSFC was requested to study earth orbit rendezvous, Langley to study lunar orbit rendezvous, and JPL to study lunar surface rendezvous. The NASA Office of Launch Vehicle Programs would provide similar information on direct ascent. Additional Details: here....

1961 August 31 - . LV Family: Saturn V. Launch Vehicle: Saturn C-3.
Chamberlain proposes lunar landing by Gemini - . Nation: USA. Program: Apollo. Class: Manned. Type: Manned spacecraft. Spacecraft: Gemini. Landing by Gemini using 4,000 kg wet/680 kg empty lander and Saturn C-3 booster. Landing by January 1966..
1961 September 5 - . Launch Site: Cape Canaveral. Launch Complex: Cape Canaveral. Launch Vehicle: Saturn V.
Purchase of land for Saturn V launch facilities. - . Nation: USA. Program: Apollo. Authorization for NASA to acquire necessary land for additional launch facilities at Cape Canaveral was approved by the Senate..
1961 September 11 - . Launch Vehicle: Saturn V.
North American selected to build S-II stage. - . Nation: USA. Related Persons: von Braun. Program: Apollo. Spacecraft: Apollo Lunar Landing.
NASA selected NAA to develop the second stage (S-II) for the advanced Saturn launch vehicle. The cost, including development of at least ten vehicles, would total about $140 million. The S-II configuration provided for four J-2 liquid-oxygen - liquid-hydrogen engines, each delivering 200,000 pounds of thrust.

1961 September 17 - . Launch Vehicle: Saturn V.
36 companies invited to bid on the first stage of advanced Saturn - . Nation: USA. Program: Apollo.
NASA invited 36 companies to bid on a contract to produce the first stage of the advanced Saturn launch vehicle. Representatives of interested companies would attend a pre-proposal conference in New Orleans, La., on September 26. Bids were to be submitted by October 16 and NASA would then select the contractor, probably in November.

1961 September 25 - . Launch Vehicle: Saturn V.
S-IC fabrication plant manager named. - . Nation: USA. Related Persons: von Braun. Program: Apollo. Dr. George N. Constan of Marshall Space Flight Center named as acting manager of the new NASA Saturn fabrication plant near New Orleans by Director von Braun of Marshall Space Flight Center..
1961 September 26 - . Launch Vehicle: Saturn V.
Bidders conference for S-IC stage. - . Nation: USA. Program: Apollo. Spacecraft: Apollo Lunar Landing. NASA bidders conference on a contract to produce the booster (S-I) stage of the Saturn vehicle was held at the Municipal Auditorium, New Orleans..
1961 October 3 - . Launch Vehicle: Saturn V.
S- IVB stage to have a single J-2 engine - . Nation: USA. Program: Apollo.
The MSFC-STG Space Vehicle Board at NASA Headquarters discussed the S- IVB stage, which would be modified by the Douglas Aircraft Company to replace the six LR-115 engines with a single J-2 engine. Funds of $500,000 were allocated for this study to be completed in March 1962. Additional Details: here....

1961 November 6 - . Launch Vehicle: Saturn V.
Saturn S-II to use five J-2 engines - . Nation: USA. Program: Apollo. Marshall Space Flight Center directed NAA to redesign the advanced Saturn second stage (S-II) to incorporate five rather than four J-2 engines, to provide a million pounds of thrust..
1961 November 16 - . Launch Vehicle: Saturn V.
Second decision on launch vehicles - . Nation: USA. Related Persons: McNamara, von Braun, Webb. Program: Apollo. Class: Manned. Type: Manned space station.
Golovin Committe studies launch vehicles through summer, but found the issue to be completely entertwined with mode (earth-orbit, lunar-orbit, lunar-surface rendezvous or direct flight. Two factions: large solids for direct flight; all-chemical with 4 or 5 F-1's in first stage for rendezvous options. In the end Webb and McNamara ordered development of C-4 and as a backup, in case of failure of F-1 in development, build of 6.1 m+ solid rocket motors by USAF.

1961 November 20 - . LV Family: Saturn V. Launch Vehicle: Saturn C-5.
Rosen Group recommends direct ascent for the lunar landing mission mode - . Nation: USA. Related Persons: Holmes, Brainard, Rosen, Milton. Program: Apollo. Milton W. Rosen, Director of Launch Vehicles and Propulsion, NASA Office of Manned Space Flight (OMSF), submitted to D. Brainerd Holmes, Director, OMSF, the report of the working group which had been set up on November 6.. Additional Details: here....
1961 November 29-30 - . Launch Vehicle: Saturn V.
Emergency switchover from Saturn to Apollo guidance as backup discussed - . Nation: USA. Program: Apollo. Spacecraft: Apollo CSM, CSM Guidance. On a visit to Marshall Space Flight Center by MIT Instrumentation Laboratory representatives, the possibility was discussed of emergency switchover from Saturn to Apollo guidance systems as backup for launch vehicle guidance..
1961 December 4 - . Launch Vehicle: Saturn V.
Rosen working group on launch vehicles - . Nation: USA. Related Persons: Holmes, Brainard, Rosen, Milton. Program: Apollo.
NASA Associate Administrator Robert C. Seamans, Jr., commented to D. Brainerd Holmes, Director, Office of Manned Space Flight, on the report of the Rosen working group on launch vehicles, which had been submitted on November 20. Seamans expressed himself as essentially in accord with the group's recommendations.

1961 December 15 - . Launch Vehicle: Saturn V.
Boeing named contractor for Saturn C-5 first stage (S-IC) - . Nation: USA. Related Persons: von Braun. Program: Apollo. Spacecraft: Apollo Lunar Landing.
NASA announced that The Boeing Company had been selected for negotiations as a possible prime contractor for the first stage (S-IC) of the advanced Saturn launch vehicle. The S-IC stage, powered by five F-1 engines, would be 35 feet in diameter and about 140 feet high. The $300-million contract, to run through 1966, called for the development, construction, and testing of 24 flight stages and one ground test stage. The booster would be assembled at the NASA Michoud Operations Plant near New Orleans, La., under the direction of the Marshall Space Flight Center.

1961 December 20 - . Launch Vehicle: Saturn V.
Douglas named contractor for Saturn S-IVB stage - . Nation: USA. Related Persons: von Braun. Program: Apollo. Spacecraft: Apollo Lunar Landing.
NASA announced that Douglas Aircraft had been selected for negotiation of a contract to modify the Saturn S-IV stage by installing a single 200,000-pound-thrust, Rocketdyne J-2 liquid-hydrogen/liquid-oxygen engine instead of six 15,000-pound-thrust P. & W. hydrogen/oxygen engines. Known as S-IVB, this modified stage will be used in advanced Saturn configurations for manned circumlunar Apollo missions.

1962 January 5 - . Launch Vehicle: Saturn V.
Three-man Apollo spacecraft, Saturn C-5 launch vehicle announced - . Nation: USA. Program: Apollo. Spacecraft: Apollo Lunar Landing. NASA made public the drawings of the three-man Apollo spacecraft to be used in the lunar landing development program, On January 9, NASA announced its decision that the Saturn C-5 would be the lunar launch vehicle..
1962 February 14 - . Launch Vehicle: Saturn V.
Initial contract with Boeing leading to the first stage S-IC of the Saturn C-5 - . Nation: USA. Program: Apollo.
NASA signed a contract with The Boeing Company for indoctrination, familiarization, and planning, expected to lead to a follow-on contract for design, development, manufacture, test, and launch operations of the first stage S-IC of the Saturn C-5 launch vehicle.

1962 March 18 - . Launch Vehicle: Saturn V.
Saturn C-5 first launch scheduled in the last quarter of 1965 - . Nation: USA. Related Persons: von Braun. Program: Apollo.
Marshall Space Flight Center's latest schedule on the Saturn C-5 called for the first launch in the last quarter of 1965 and the first manned launch in the last quarter of 1967. If the C-5 could be man-rated on the eighth research and development flight in the second quarter of 1967, the spacecraft lead time would be substantially reduced.

1962 April 2-3 - . Launch Vehicle: Saturn V.
Meeting at NASA Headquarters reviews the lunar orbit rendezvous (LOR) technique for Project Apollo - . Nation: USA. Related Persons: Geissler, Horn, Maynard, Shea. Program: Apollo. Spacecraft: Apollo CSM, Apollo Lunar Landing, CSM LES, CSM Recovery, CSM SPS, CSM Television.
A meeting to review the lunar orbit rendezvous (LOR) technique as a possible mission mode for Project Apollo was held at NASA Headquarters. Representatives from various NASA offices attended: Joseph F. Shea, Eldon W. Hall, William A. Lee, Douglas R. Lord, James E. O'Neill, James Turnock, Richard J. Hayes, Richard C. Henry, and Melvyn Savage of NASA Headquarters; Friedrich O. Vonbun of Goddard Space Flight Center (GSFC); Harris M. Schurmeier of Jet Propulsion Laboratory; Arthur V. Zimmeman of Lewis Research Center; Jack Funk, Charles W. Mathews, Owen E. Maynard, and William F. Rector of MSC; Paul J. DeFries, Ernst D. Geissler, and Helmut J. Horn of Marshall Space Flight Center (MSFC); Clinton E. Brown, John C. Houbolt, and William H. Michael, Jr., of Langley Research Center; and Merrill H. Mead of Ames Research Center. Each phase of the LOR mission was discussed separately.

The launch vehicle required was a single Saturn C-5, consisting of the S-IC, S-II, and S-IVB stages. To provide a maximum launch window, a low earth parking orbit was recommended. For greater reliability, the two-stage-to-orbit technique was recommended rather than requiring reignition of the S-IVB to escape from parking orbit.

The current concepts of the Apollo command and service modules would not be altered. The lunar excursion vehicle (LEV), under intensive study in 1961, would be aft of the service module and in front of the S-IVB stage. For crew safety, an escape tower would be used during launch. Access to the LEV would be provided while the entire vehicle was on the launch pad.

Both Apollo and Saturn guidance and control systems would be operating during the launch phase. The Saturn guidance and control system in the S-IVB would be "primary" for injection into the earth parking orbit and from earth orbit to escape. Provisions for takeover of the Saturn guidance and control system should be provided in the command module. Ground tracking was necessary during launch and establishment of the parking orbit, MSFC and GSFC would study the altitude and type of low earth orbit.

The LEV would be moved in front of the command module "early" in the translunar trajectory. After the S-IVB was staged off the spacecraft following injection into the translunar trajectory, the service module would be used for midcourse corrections. Current plans were for five such corrections. If possible, a symmetric configuration along the vertical center line of the vehicle would be considered for the LEV. Ingress to the LEV from the command module should be possible during the translunar phase. The LEV would have a pressurized cabin capability during the translunar phase. A "hard dock" mechanism was considered, possibly using the support structure needed for the launch escape tower. The mechanism for relocation of the LEV to the top of the command module required further study. Two possibilities were discussed: mechanical linkage and rotating the command module by use of the attitude control system. The S-IVB could be used to stabilize the LEV during this maneuver.

The service module propulsion would be used to decelerate the spacecraft into a lunar orbit. Selection of the altitude and type of lunar orbit needed more study, although a 100-nautical-mile orbit seemed desirable for abort considerations.

The LEV would have a "point" landing (±½ mile) capability. The landing site, selected before liftoff, would previously have been examined by unmanned instrumented spacecraft. It was agreed that the LEV would have redundant guidance and control capability for each phase of the lunar maneuvers. Two types of LEV guidance and control systems were recommended for further analysis. These were an automatic system employing an inertial platform plus radio aids and a manually controlled system which could be used if the automatic system failed or as a primary system.

The service module would provide the prime propulsion for establishing the entire spacecraft in lunar orbit and for escape from the lunar orbit to earth trajectory. The LEV propulsion system was discussed and the general consensus was that this area would require further study. It was agreed that the propulsion system should have a hover capability near the lunar surface but that this requirement also needed more study.

It was recommended that two men be in the LEV, which would descend to the lunar surface, and that both men should be able to leave the LEV at the same time. It was agreed that the LEV should have a pressurized cabin which would have the capability for one week's operation, even though a normal LOR mission would be 24 hours. The question of lunar stay time was discussed and it was agreed that Langley should continue to analyze the situation. Requirements for sterilization procedures were discussed and referred for further study. The time for lunar landing was not resolved.

In the discussion of rendezvous requirements, it was agreed that two systems be studied, one automatic and one providing for a degree of manual capability. A line of sight between the LEV and the orbiting spacecraft should exist before lunar takeoff. A question about hard-docking or soft-docking technique brought up the possibility of keeping the LEV attached to the spacecraft during the transearth phase. This procedure would provide some command module subsystem redundancy.

Direct link communications from earth to the LEV and from earth to the spacecraft, except when it was in the shadow of the moon, was recommended. Voice communications should be provided from the earth to the lunar surface and the possibility of television coverage would be considered.

A number of problems associated with the proposed mission plan were outlined for NASA Center investigation. Work on most of the problems was already under way and the needed information was expected to be compiled in about one month.

(This meeting, like the one held February 13-15, was part of a continuing effort to select the lunar mission mode).

1962 April 24 - . Launch Vehicle: Saturn V.
Rosen recommends Saturn C-5 design and lunar orbit rendezvous - . Nation: USA. Related Persons: Rosen, Milton. Program: Apollo. Spacecraft: Apollo LM, Apollo Lunar Landing, CSM Recovery, LM Mode Debate, LM Source Selection.
Milton W. Rosen, NASA Office of Manned Space Flight Director of Launch Vehicles and Propulsion, recommended that the S-IVB stage be designed specifically as the third stage of the Saturn C-5 and that the C-5 be designed specifically for the manned lunar landing using the lunar orbit rendezvous technique. The S-IVB stage would inject the spacecraft into a parking orbit and would be restarted in space to place the lunar mission payload into a translunar trajectory. Rosen also recommended that the S- IVB stage be used as a flight test vehicle to exercise the command module (CM), service module (SM), and lunar excursion module (LEM) (previously referred to as the lunar excursion vehicle (LEV)) in earth orbit missions. The Saturn C-1 vehicle, in combination with the CM, SM, LEM, and S-IVB stage, would be used on the most realistic mission simulation possible. This combination would also permit the most nearly complete operational mating of the CM, SM, LEM, and S-IVB prior to actual mission flight.

1962 May 26 - . Launch Vehicle: Saturn V.
Saturn F-1 engine first fired at full power - . Nation: USA. Program: Apollo. The F-1 engine was first fired at full power more than 1.5 million pounds of thrust) for 2.5 minutes at Edwards Rocket Site, Calif..
1962 May 29 - . Launch Vehicle: Saturn V.
Mobile launcher concept for the Saturn C-5 approved - . Nation: USA. Program: Apollo. The Manned Space Flight Management Council approved the mobile launcher concept for the Saturn C-5 at Launch Complex 39, Merritt Island, Fla..
1962 June - . Launch Vehicle: Saturn V.
Study of repair of J-2 engine in space - . Nation: USA. Program: Apollo. Spacecraft: Apollo CSM.
Five NASA scientists, dressed in pressure suits, completed an exploratory study at Rocketdyne Division of the feasibility of repairing, replacing, maintaining, and adjusting components of the J-2 rocket while in space. The scientific team also investigated the design of special maintenance tools and the effectiveness of different pressure suits in performing maintenance work in space.

1962 July 2 - . Launch Vehicle: Saturn V.
Contracts to Rocketdyne for production of the Saturn's F-1 and J-2 rocket engines - . Nation: USA. Program: Apollo. NASA awarded three contracts totaling an estimated $289 million to NAA's Rocketdyne Division for the further development and production of the F-1 and J-2 rocket engines..
1962 July 21 - . Launch Vehicle: Saturn V.
Apollo advanced Saturn launch complex northwest of Cape Canaveral - . Nation: USA. Program: Apollo.
NASA announced plans for an advanced Saturn launch complex to be built on 80,000 acres northwest of Cape Canaveral. The new facility, Launch Complex 39, would include a building large enough for the vertical assembly of a complete Saturn launch vehicle and Apollo spacecraft.

1962 August 8 - . Launch Vehicle: Saturn V.
Contract to Douglas for the S-IVB stage - . Nation: USA. Related Persons: von Braun. Program: Apollo.
NASA awarded a $141.1 million contract to the Douglas Aircraft Company for design, development, fabrication, and testing of the S-IVB stage, the third stage of the Saturn C-5 launch vehicle. The contract called for 11 S-IVB units, including three for ground tests, two for inert flight, and six for powered flight.

1962 August - . Launch Vehicle: Saturn V.
Structural requirements for Apollo lunar excursion module adapter established - . Nation: USA. Program: Apollo. NAA finished structural requirements for a lunar excursion module adapter mating the 154-inch diameter service module to the 260-inch diameter S-IVB stage..
1962 September 26 - . Launch Vehicle: Saturn V.
Plans for Apollo Mississippi Test Facility - . Nation: USA. Program: Apollo.
NASA announced that it had completed preliminary plans for the development of the $500-million Mississippi Test Facility. The first phase of a three-phase construction program would begin in 1962 and would include four test stands for static-firing the Saturn C-5 S-IC and S-II stages; about 20 support and service buildings would be built in the first phase. A water transportation system had been selected, calling for improvement of about 15 miles of river channel and construction of about 15 miles of canals at the facility. Additional Details: here....

1962 September - . Launch Vehicle: Saturn V.
Apollo spacecraft weights - . Nation: USA. Program: Apollo. Spacecraft: Apollo CSM, LM Weight.
The Apollo spacecraft weights had been apportioned within an assumed 90,000 pound limit. This weight was termed a "design allowable." A lower target weight for each module had been assigned. Achievement of the target weight would allow for increased fuel loading and therefore greater operational flexibility and mission reliability. The design allowable for the command module was 9,500 pounds; the target weight was 8,500 pounds. The service module design allowable was 11,500 pounds; the target weight was 11,000 pounds. The S-IVB adapter design allowable and target weight was 3,200 pounds. The amount of service module useful propellant was 40,300 pounds design allowable; the target weight was 37,120 pounds. The lunar excursion module design allowable was 25,500 pounds; the target weight was 24,500 pounds.

1962 October 4 - . Launch Vehicle: Saturn V.
First full-duration static firing of the Apollo J-2 engine - . Nation: USA. Program: Apollo. Rocketdyne Division successfully completed the first full-duration (250-seconds) static firing of the J-2 engine..
1962 October 30 - . Launch Vehicle: Saturn V.
Contract for production of the S-II stage signed - . Nation: USA. Program: Apollo.
NASA announced the signing of a contract with the Space and Information Systems Division of NAA for the development and production of the second stage (S-II) of the Saturn C-5 launch vehicle. The $319.9-million contract, under the direction of Marshall Space Flight Center, covered the production of nine live flight stages, one inert flight stage, and several ground-test units for the advanced Saturn launch vehicle. NAA had been selected on September 11, 1961, to develop the S-II.

1962 October - . Launch Vehicle: Saturn V.
Technique for separating the Apollo command and service modules during an abort - . Nation: USA. Program: Apollo. Spacecraft: Apollo CSM, CSM RCS.
The technique tentatively selected by NAA for separating the command and service modules from lower stages during an abort consisted of firing four 2000-pound-thrust posigrade rockets mounted on the service module adapter. With this technique, no retrorockets would be needed on the S-IV or S-IVB stages. Normal separation from the S-IVB would be accomplished with the service module reaction control system.

1962 October 31 - . Launch Vehicle: Saturn V.
Contract for the S-IVB stage for use in the Saturn C- 1B - . Nation: USA. Program: Apollo. NASA announced that the Douglas Aircraft Company had been awarded a $2.25million contract to modify the S-IVB stage for use in the Saturn C- 1B program..
1962 December 3 - . Launch Vehicle: Saturn V.
Four firms to design the Apollo Vertical Assembly Building (VAB) - . Nation: USA. Program: Apollo.
The U.S. Army Corps of Engineers, acting for NASA, awarded a $3.332 million contract to four New York architectural engineering firms to design the Vertical Assembly Building (VAB) at Cape Canaveral. The massive VAB became a space-age hangar, capable of housing four complete Saturn V launch vehicles and Apollo spacecraft where they could be assembled and checked out. The facility would be 158.5 meters (520 feet high) and would cost about $100 million to build. Subsequently, the Corps of Engineers selected Morrison-Knudson Company, Perini Corp., and Paul Hardeman, Inc., to construct tile VAB.

1962 December 4 - . Launch Vehicle: Saturn V.
First test of the Apollo main parachute system - . Nation: USA. Program: Apollo.
The first test of the Apollo main parachute system, conducted at the Naval Air Facility, El Centro, Calif., foreshadowed lengthy troubles with the landing apparatus for the spacecraft. One parachute failed to inflate fully, another disreefed prematurely, and the third disreefed and inflated only after some delay. No data reduction was possible because of poor telemetry. North American was investigating.

1963 January 22 - . Launch Vehicle: Saturn V.
Orbiting Space Station. - . Nation: USA. Program: Skylab. Spacecraft: LORL.
Addressing an Institute of Aerospace Science meeting in New York, George von Tiesenhausen, Chief of Future Studies at NASA's Launch Operations Center, stated that by 1970 the United States would need an orbiting space station to launch and repair spacecraft. The station could also serve as a manned scientific laboratory. In describing the 91-m-long, 10-m-diameter structure, von Tiesenhausen said that the station could be launched in two sections using Saturn C-5 vehicles. The sections would be joined once in orbit.

1963 February 12 - . Launch Vehicle: Saturn V.
Marion Power Shovel selected to build the Saturn V crawler-transport - . Nation: USA. Program: Apollo.
NASA selected the Marion Power Shovel Company to design and build the crawler-transport, a device to haul the Apollo space vehicle (Saturn V, complete with spacecraft and associated launch equipment) from the Vertical Assembly Building to the Merritt Island, Fla., launch pad, a distance of about 5.6 kilometers (3.5 miles). The crawler would be 39.6 meters (130 feet) long, 35 meters (115 feet) wide, and 6 meters (20 feet) high, and would weight 2.5 million kilograms (5.5 million pounds). NASA planned to buy two crawlers at a cost of $4 to 5 million each. Formal negotiations began on February 20 and the contract was signed on March 29.

1963 February 25 - . Launch Vehicle: Saturn V.
Formal contract with Boeing for the S-IC - . Nation: USA. Program: Apollo.
NASA announced the signing of a formal contract with The Boeing Company for the S-IC (first stage) of the Saturn V launch vehicle, the largest rocket unit under development in the United States. The $418,820,967 agreement called for the development and manufacture of one ground test and ten flight articles. Preliminary development of the S-IC, which was powered by five F-1 engines, had been in progress since December 1961 under a $50 million interim contract. Booster fabrication would take place primarily at the Michoud Operations Plant, New Orleans, La., but some advance testing would be done at MSFC and the Mississippi Test Operations facility.

1963 April 17 - . LV Family: Saturn V, Saturn I, Titan.
Large Solid Rocket Motor Program (Program 623A) begun. - .
The Defense Department announced the selection of Thiokol Chemical Corporation, Aerojet-General Corporation, and Lockheed Propulsion Company to conduct work on the development of large solid-propellant motors as part of the Space Systems Division's Large Solid Rocket Motor Program (Program 623A). Development work was divided into four tasks: (1) Thiokol and Aerojet-General were to develop 260-inch diameter, solid rocket motors of 3 million pounds of thrust for demonstration static firings; (2) Thiokol was to work on a 156-inch, 3 million-pound thrust, two-segment solid rocket motor; (3) Thiokol was to develop and static fire a 156-inch, one-segment solid rocket motor of one million pounds thrust demonstrating thrust vector control (TVC) through movable nozzles; and (4) Lockheed was to static fire a 156-inch, single segment solid rocket motor of one million pounds thrust that demonstrated TVC through jet tabs.

1963 April 30 - . Launch Vehicle: Saturn V.
Earth parking orbit requirements - . Nation: USA. Program: Apollo.
The Apollo Spacecraft Mission Trajectory Sub-Panel discussed earth parking orbit requirements for the lunar mission. The maximum number of orbits was fixed by the S-IVB's 4.5-hour duration limit. Normally, translunar injection (TLI) would be made during the second orbit. The panel directed North American to investigate the trajectory that would result from injection from the third, or contingency, orbit. The contractor's study must reckon also with the effects of a contingency TLI upon the constraints of a free return trajectory and fixed lunar landing sites.

1963 May 20-22 - . Launch Vehicle: Saturn V.
Status report on the Apollo LEM landing gear design and Apollo LEM stowage height - . Nation: USA. Program: Apollo. Spacecraft: Apollo LM, LM Landing Gear.
At a meeting on mechanical systems at MSC, Grumman presented a status report on the LEM landing gear design and LEM stowage height. On May 9, NASA had directed the contractor to consider a more favorable lunar surface than that described in the original Statement of Work. Additional Details: here....

1963 June 3 - . Launch Vehicle: Saturn V.
Length of the spacecraft-Saturn V adapter had been increased from 8.077 meters to 8.89 meters - . Nation: USA. Program: Apollo. Spacecraft: Apollo LM, LM Landing Gear. MSC informed MSFC that the length of the spacecraft-Saturn V adapter had been increased from 807.7 centimeters to 889 centimeters (318 inches to 350 inches). The LEM would be supported in the adapter from a fixed structure on the landing gear..
1963 June 25 - . Launch Vehicle: Saturn V.
Apollo LEM landing gear design freeze - . Nation: USA. Program: Apollo. Spacecraft: Apollo LM, LM Landing Gear.
MSC Director Robert R. Gilruth reported to the MSF Management Council that the LEM landing gear design freeze was now scheduled for August 31. Grumman had originally proposed a LEM configuration with five fixed legs, but LEM changes had made this concept impractical. The weight and overall height of the LEM had increased, the center of gravity had been moved upward, the LEM stability analysis had expanded to cover a wider range of landing conditions, the cruciform descent stage had been selected, and the interpretation of the lunar model had been revised. These changes necessitated a larger gear diameter than at first proposed. This, in turn, required deployable rather than fixed legs so the larger gear could be stored in the Saturn V adapter. MSC had therefore adopted a four-legged deployable gear, which was lighter and more reliable than the five-legged configuration.

1963 July 10 - . Launch Vehicle: Saturn V.
Pregnant Guppy FAA certification - . Nation: USA. Program: Apollo. Aero Spacelines' "Pregnant Guppy," a modified Boeing Stratocruiser, won airworthiness certification by the Federal Aviation Agency. The aircraft would be used to transport major Apollo spacecraft and launch vehicle components..
1963 August 2 - . Launch Vehicle: Saturn V.
Grumman to design the LEM to have a thrusting capability with the Apollo CSM attached - . Nation: USA. Program: Apollo. Spacecraft: Apollo LM, CSM SPS.
North American asked MSC if Grumman was designing the LEM to have a thrusting capability with the CSM attached and, if not, did NASA intend to require the additional effort by Grumman to provide this capability. North American had been proceeding on the assumption that, should the service propulsion system (SPS) fail during translunar flight, the LEM would make any course corrections needed to ensure a safe return trajectory. Additional Details: here....

1963 August 23 - . LV Family: Saturn V.
Headquarters Space Systems Division awarded two contracts in its program to develop the technology for large-solid-propellant motors (Program 623A). - .
Thiokol Chemical Corporation and Aerojet-General Corporation received contracts for demonstration static firings of 260-inch diameter, solid-propellant rocket motors of approximately 3 million, pounds thrust. Following the test firings, one of the contractors would be selected to continue development of the 260-inch motor.

1963 October 2 - . Launch Vehicle: Saturn V.
Preliminary configuration freeze for the Apollo LEM-adapter arrangement - . Nation: USA. Program: Apollo. Spacecraft: Apollo LM, LM Descent Propulsion, LM Landing Gear.
At a LEM Mechanical Systems Meeting in Houston, Grumman and MSC agreed upon a preliminary configuration freeze for the LEM-adapter arrangement. The adapter would be a truncated cone, 876 centimeters (345 inches) long. The LEM would be mounted inside the adapter by means of the outrigger trusses on the spacecraft's landing gear. This configuration provided ample clearance for the spacecraft, both top and bottom (i.e., between the service propulsion engine bell and the instrument unit of the S-IVB).

At this same meeting, Grumman presented a comparison of radially and laterally folded landing gears (both of 457-centimeter (180-inch) radius). The radial-fold configuration, MSC reported, promised a weight savings of 22-2 kilograms (49 pounds). MSC approved the concept, with an 876-centimeter (345-inch) adapter. Further, an adapter of that length would accommodate a larger, lateral fold gear (508 centimeters (200 inches)), if necessary. During the next several weeks, Grumman studied a variety of gear arrangements (sizes, means of deployment, stability, and even a "bending" gear). At a subsequent LEM Mechanical Systems Meeting, on November 10, Grumman presented data (design, performance, and weight) on several other four-legged gear arrangements - a 457-centimeter (180-inch), radial fold "tripod" gear (i.e., attached to the vehicle by three struts), and 406.4-centimeter (160-inch) and 457-centimeter (180-inch) cantilevered gears. As it turned out, the 406.4-centimeter (160-inch) cantilevered gear, while still meeting requirements demanded in the work statement, in several respects was more stable than the larger tripod gear. In addition to being considerably lighter, the cantilevered design offered several added advantages:

A reduced stowed height for the LEM from 336.5 to 313.7 centimeters (132.5 to 123.5 inches).
A shorter landing stroke (50.8 instead of 101.6 centimeters) (20 instead of 40 inches).
Better protection from irregularities (protuberances) on the surface.
An alleviation of the gear heating problem (caused by the descent engine's exhaust plume).
Simpler locking mechanisms.
A better capability to handle various load patterns on the landing pads.
Because of these significant (and persuasive) factors, MSC approved Grumman's change to the 406.4- centimeter (160-inch) cantilevered arrangement as the design for the LEM's landing gear. By mid- November, MSC reported to OMSF that Grumman was pursuing the 406.4-centimeter (160-inch) cantilevered gear. Although analyses would not be completed for some weeks, the design was "shown . . . to be the lightest gear available to date. . . . Tentative estimates indicate a gear stowed height reduction of about 9" (22.9 centimeters), which will still accommodate the 180" (45.7 centimeter) cantilever or 200" (508-centimeter) lateral fold gear as growth potential." Grumman's effort continued at "firming up" the design, including folding and docking mechanisms.
1963 October 15 - . Launch Vehicle: Saturn V.
Apollo Guidance and Performance Sub-Panel first meeting - . Nation: USA. Program: Apollo.
The Guidance and Performance Sub-Panel, at its first meeting, began coordinating work at MSC and MSFC. The sub-panel outlined tasks for eac Center: MSFC would define the dispersions comprising the launch vehicle performance reserves, prepare a set of typical translunar injection errors for the Saturn V launch vehicle, and give MSC a typical Saturn V guidance computation for injection into an earth parking orbit. MSC would identify the constraints required for free-return trajectories and provide MSFC with details of the MIT guidance method. Further, the two Centers would exchange data each month showing current launch vehicle and spacecraft performance capability. (For operational vehicles, studies of other than performance capability would be based on control weights and would not reflect the current weight status.)

1963 October 31 - . Launch Vehicle: Saturn V.
First production F-1 engine delivered - . Nation: USA. Program: Apollo. The first production F-1 engine for the Apollo Saturn V was flown from Rocketdyne's Canoga Park, Calif., facility, where it was manufactured, to MSFC aboard Aero Spacelines' "Pregnant Guppy.".
1963 November 12 - . Launch Vehicle: Saturn V.
Supplemental agreement for the S-IC stage of the Saturn V launch vehicle - . Nation: USA. Program: Apollo. The Boeing Company and NASA signed a $27.4 million supplemental agreement to the contract for development, fabrication, and test of the S-IC (first) stage of the Saturn V launch vehicle..
1963 November 12 - . Launch Vehicle: Saturn V.
Contract for the construction of Saturn V LC-39A - . Nation: USA. Program: Apollo. NASA awarded a $19.2 million contract to Blount Brothers Corporation and M. M. Sundt Construction Company for the construction of Pad A, part of the Saturn V Launch Complex 39 at LOC..
1963 November 27 - . Launch Vehicle: Saturn V.
First long-duration test firing of Apollo J-2 engine - . Nation: USA. Program: Apollo. At its Santa Susana facility, Rocketdyne conducted the first long-duration (508 seconds) test firing of a J-2 engine. In May 1962 the J-2's required firing time was increased from 250 to 500 seconds..
1963 December 9 - . Launch Vehicle: Saturn V.
Space required in the S-IVB instrument unit for different Apollo LEM landing gear designs defined - . Nation: USA. Program: Apollo. ASPO requested that Grumman make a layout for transmittal to MSFC showing space required in the S-IVB instrument unit for 406.4- and 457-centimeter (160- and 180-inch) cantilevered gears and for 508-centimeter (200-inch)-radius lateral fold gears..
1963 December 26 - . Launch Vehicle: Saturn V.
Extension of Apollo systems to permit more extensive exploration of the lunar surface. - . Nation: USA. Related Persons: Shea, von Braun. Spacecraft: Apollo LM Shelter, Apollo LM Taxi.
MSFC Director Wernher von Braun described to Apollo Spacecraft Program Manager Joseph F. Shea a possible extension of Apollo systems to permit more extensive exploration of the lunar surface. Huntsville's concept, called the Integrated Lunar Exploration System, involved a dual Saturn V mission (with rendezvous in lunar orbit) to deliver an integrated lunar taxi/shelter spacecraft to the Moon's surface. Additional Details: here....

1964 February 26 - . Launch Vehicle: Saturn V.
Lockheed recommendations on a scientific space station program. - . Nation: USA. Spacecraft: LORL.
The Lockheed-California Company released details of its recommendations to MSC on a scientific space station program. The study concluded that a manned station with a crew of 24 could be orbiting the Earth in 1968. Total cost of the program including logistics spacecraft and ground support was estimated at $2.6 billion for five years' operation. Lockheed's study recommended the use of a Saturn V to launch the unmanned laboratory into orbit and then launching a manned logistics vehicle to rendezvous and dock at the station.

1964 March 30 - . Launch Vehicle: Saturn V.
Contract for production of 76 F-1 engines - . Nation: USA. Program: Apollo. MSFC awarded Rocketdyne a definitive contract (valued at $158.4 million) for the production of 76 F-1 engines for the first stage of the Saturn V launch vehicle and for delivery of ground support equipment..
1964 April - . Launch Vehicle: Saturn V.
Rotating manned orbital research laboratory for a Saturn V launch vehicle. - . Nation: USA. Program: Skylab. Spacecraft: LORL.
A study to recommend, define, and substantiate a logical approach for establishing a rotating manned orbital research laboratory for a Saturn V launch vehicle was made for MSC. The study was performed by the Lockheed-California Company, Burbank, California. It was based on the proposition that a large rotating space station would be one method by which the United States could maintain its position as a leader in space technology. Additional Details: here....

1964 September 10 - . LV Family: Saturn V.
NASA announced that its Lewis Research Center (LeRC) would assumed management responsibility for the large solid-rocket motor development program. - .
NASA would take over the 260-inch diameter solid-motor development program from Space Systems Division, and the Aerojet-General and Thiokol developed contracts initiated by SSD in June 1963 were to be transferred to NASA. The 156-inch diameter solid-motor program would remain under SSD control.

1964 October 2 - . Launch Vehicle: Saturn V.
Plan to verify the Apollo CM's radiation shielding - . Nation: USA. Program: Apollo. Spacecraft: Apollo CSM, CSM Block II.
MSC's Apollo Spacecraft Program Office (ASPO) approved a plan (put forward by the MSC Advanced Spacecraft Technology Division to verify the CM's radiation shielding. Checkout of the radiation instrumentation would be made during manned earth orbital flights. The spacecraft would then be subjected to a radiation environment during the first two unmanned Saturn V flights. These missions, 501 and 502, with apogees of about 18,520 km (10,000 nm), would verify the shielding. Gamma probe verification, using spacecraft 008, would be performed in Houston during 1966. Only Block I CM's would be used in these ground and flight tests. Radiation shielding would be unaffected by the change to Block II status.

1964 October 15 - . Launch Vehicle: Saturn V.
Apollo guidance and control interfaces - . Nation: USA. Program: Apollo. Spacecraft: Apollo CSM, CSM Block II.
The Guidance and Control Implementation Sub-Panel of the MSC-MSFC Flight Mechanics Panel defined the guidance and control interfaces for Block I and II missions. In Block II missions the CSM's guidance system would guide the three stages of the Saturn V vehicle; it would control the S- IVB (third stage) and the CSM while in earth orbit; and it would perform the injection into a lunar trajectory. In all of this, the CSM guidance backed up the Saturn ST-124 platform. Actual sequencing was performed by the Saturn V computer.

1964 November 12-19 - . Launch Vehicle: Saturn V.
Disagreement on number of reentry tests to qualify Apollo CM heatshield - . Nation: USA. Program: Apollo. Spacecraft: Apollo CSM, CSM Heat Shield.
There appeared to be some confusion and/or disagreement concerning whether one or two successful Saturn V reentry tests were required to qualify the CM heatshield. A number of documents relating to instrumentation planning for the 501 and 502 flight indicated that two successful reentries would be required. The preliminary mission requirements document indicated that only a single successful reentry trajectory would be necessary. The decision would influence the measurement range capability of some heatshield transducers and the mission planning activity being conducted by the Apollo Trajectory Support Office. The Structures and Mechanics Division had been requested to provide Systems Engineering with its recommendation.

1964 November 19-26 - . Launch Vehicle: Saturn V.
Apollo procedural rules for translunar injection - . Nation: USA. Program: Apollo.
The MSC-Marshall Space Flight Center (MSFC) Guidance and Control Implementation Sub-Panel set forth several procedural rules for translunar injection (TLI):

Once the S-IVB ignition sequence was started, the spacecraft would not be able to halt the maneuver. (This would occur about 427 sec before the stage's J-2 engine achieved 90 percent of its thrust capability.)
Because the spacecraft would receive no signal from the instrument unit (IU), the exact time of sequence initiation must be relayed from the ground.
The vehicle's roll attitude would be reset prior to injection.
And when the spacecraft had control of the vehicle, the IU would not initiate the ignition sequence.
1964 December 4 - . Launch Vehicle: Saturn V.
Battleship S-IVB second stage static-fired - . Nation: USA. Program: Apollo.
At its Sacramento test site, Douglas Aircraft Company static-fired a "battleship" S-IVB second stage of the Saturn IB vehicle, for 10 sec. (A battleship rocket stage was roughly the vehicle's equivalent to a boilerplate spacecraft.) On January 4, 1965, after further testing of the stage's J-2 engine, the stage underwent its first full-duration firing, 480 sec.

1964 December 7 - . Launch Vehicle: Saturn V.
First S-IVB stage delivered for testing - . Nation: USA. Program: Apollo.
Douglas Aircraft Company delivered the first S-IVB stage to Marshall Space Flight Center for extensive vibration, bending, and torsional testing. The stage was not an actual flight stage and contained mockups of the engine and other components, but it duplicated the flight article in weight, mass, center of gravity, and stiffness.

1965 January 5 - . Launch Vehicle: Saturn V.
Apollo trajectory with a launch azimuth of 108 degrees - . Nation: USA. Program: Apollo.
At the fourth meeting of the Reference Trajectory Sub-Panel, MSC and MSFC members agreed on a trajectory with a launch azimuth of 108 degrees. Translunar injection would be performed over the Pacific Ocean during the first or second orbits. First-orbit injection would fix the minimum time required before the maneuver. Injection on the second pass would determine consequent penalties. The actions were initiated by Mission Planning and Analysis Division (MPAD) and were required to solidify and minimize analytical studies and operational planning.

1965 January 14-21 - . Launch Vehicle: Saturn V.
S-IVB Stage attitude control capability - . Nation: USA. Program: Apollo.
Significant agreements from the Eleventh MSC-MSFC Flight Mechanics, Dynamics, Guidance and Control Panel meeting were:

There was no requirement to inhibit the S-IVB attitude and attitude rate hold modes during the transposition and docking phase.
The S-IVB auxiliary propulsion system had sufficient propellant to perform 21 roll maneuvers in earth orbit at 0.5 deg/sec for inertial measurement unit alignment and earth landmark sightings, one yaw maneuver at 0.3 deg/sec for sun avoidance before transposition and docking, and one pitch and or yaw maneuver at 0.3 deg/sec before the final CSM/LEM separation maneuver from the S-IVB.
1965 January 23 - . Launch Vehicle: Saturn V.
Technique for Apollo LEM / S-IVB separation during manned mission approved - . Nation: USA. Program: Apollo. Spacecraft: Apollo LM, CSM Electrical, LM Electrical.
ASPO approved the technique for LEM S-IVB separation during manned missions, a method recommended jointly by North American and Grumman. After the CSM docked with the LEM, the necessary electrical circuit between the two spacecraft would be closed manually. Explosive charges would then free the LEM from the adapter on the S-IVB.

1965 January 28 - . Launch Vehicle: Saturn V.
First major Saturn V flight component delivered - . Nation: USA. Program: Apollo.
The first major Saturn V flight component, a 10-m (33-ft) diameter, 27,215 kg (60,000 lb corrugated tail section which would support the booster's 6,672 kilonewtons (1.5-million-lb) thrust engines, arrived at MSFC from NASA's Michoud Operations near New Orleans. The section was one of five major structural units comprising Saturn V's first stage.

1965 February 9 - . Launch Vehicle: Saturn V.
First ground test model of the S-II stage completed - . Nation: USA. Program: Apollo. North American completed the first ground test model of the S-II stage of the Saturn V..
1965 February 19 - . Launch Vehicle: Saturn V.
Deployment angle of the Apollo adapter panels changed - . Nation: USA. Program: Apollo. Spacecraft: Apollo LM, CSM Block II, LM Communications.
To eliminate interference between the S-IVB stage and the instrument unit, MSC directed North American to modify the deployment angle of the adapter panels. Originally designed to rotate 170 degrees, the panels should open but 45 degrees (60 degrees during abort), where they were to be secured while the CSM docked with and extracted the LEM.

But at this smaller angle, the panels now blocked the CM's four flush- mounted omnidirectional antennas, used during near-earth phases of the mission. While turning around and docking, the astronauts thus had to communicate with the ground via the steerable high gain antenna. For Block II spacecraft, therefore, MSC concurrently ordered North American to broaden the S-band equipment's capability to permit it to operate within 4,630 km (2,500 nm) of earth.

1965 February 27 - . LV Family: Saturn V, Saturn I.
The Thiokol Chemical Corporation (Brunswick Division) static-fired a two-segment, 156-inch diameter, 100-foot long solid-propellant rocket motor (156-2-T). - .
This 900,000-pound motor, the largest solid-propellant motor yet fired, generated over three million pounds of thrust for one minute, more than twice as much as any previous motor. This test firing was intended to validate design criteria for the 260-inch motor program that was officially transferred from Space Systems Division management to that of NASA's Lewis Research Center (LeRC) on 1 March.

1965 March 8 - . Launch Vehicle: Saturn V.
No serious weight problems with the Apollo spacecraft - . Nation: USA. Related Persons: Shea. Program: Apollo. Spacecraft: Apollo LM, LM Weight.
Missiles and Rockets reported a statement by Joseph F. Shea, ASPO manager, that MSC had no serious weight problems with the Apollo spacecraft. The current weight, he said, was 454 kg (1,000 lbs) under the 40,823 kg (90,000 lb) goal. Moreover, the increased payload of the Saturn V to 43,091 kg (95,000 lbs) permitted further increases. Shea admitted, however, that the LEM was growing; recent decisions in favor of safety and redundancy could raise the module's weight from 13,381 kg to 14,575 kg (29,500 lbs to 32,000 lbs).

1965 April 13 - . Launch Vehicle: Saturn V.
Environmental testing of a full-scale Apollo S-IVB stage simulator - . Nation: USA. Program: Apollo.
Marshall Space Flight Center finalized a $2,697,546 addition to an existing contract with Douglas Aircraft Company to provide for environmental testing of a full-scale S-IVB forward stage simulator, a full-scale test instrument unit, and an Apollo thermal simulator. Testing would be conducted in Douglas' 11.89-m- (39-ft-) diameter space simulator at Huntington Beach, California, and would simulate a typical Saturn V flight from launch to earth orbit and injection into lunar path.

1965 April 14 - . Launch Vehicle: Saturn V.
Final beam in the structural skeleton of the Vertical Assembly Building - . Nation: USA. Program: Apollo.
Construction workers emplaced the final beam in the structural skeleton of the Vertical Assembly Building at Merritt Island (KSC), Florida. Scheduled for completion in 1966, the cavernous structure (160 m (525 ft) tall and comprising 10,968,476 cu m (129 million cu ft)) would provide a controlled environment for assembling Saturn V launch vehicles and mating them to Apollo spacecraft.

1965 April 15 - . Launch Vehicle: Saturn V.
First ground test firing of S-II stage - . Nation: USA. Program: Apollo.
1965 April 16 - . Launch Vehicle: Saturn V.
First clustered firing of Saturn V's first stage - . Nation: USA. Program: Apollo.
MSFC conducted the first clustered firing of the Saturn V's first stage (the S-IC). The booster's five F-1 engines burned for about 6½ seconds and produced 33,360 kilonewtons (7.5 million lbs) thrust.

Eight days later, at its static facility in Santa Susana, California, North American first fired the S-II, intermediate stage of the Saturn V. The event was chronicled as the "second major Saturn V milestone" during April. Additional Details: here....

1965 April 20 - . Launch Vehicle: Saturn V.
NASA and Boeing negotiated an Apollo contract modification - . Nation: USA. Program: Apollo. NASA and Boeing negotiated a contract modification. For an additional $3,135,977, Boeing would furnish instrumentation equipment and engineering support for Marshall Space Flight Center's program for dynamic testing of the Saturn V..
1965 June 21 - . Launch Vehicle: Saturn V.
1,000th test firing of the F-1 engine - . Nation: USA. Program: Apollo. North American's Rocketdyne Division conducted the 1,000th test firing of the Saturn V's first-stage engine, the F-1..
1965 June 25 - . Launch Vehicle: Saturn V.
Nine additional S-IVB stages for the Saturn V - . Nation: USA. Program: Apollo.
NASA announced negotiations with Douglas Aircraft Company for nine additional S-IVB stages to be used as the third stage of the Saturn V launch vehicle being developed at Marshall Space Flight Center. Work was to include related spares and launch support services. The S-IVB contract, presently valued at $312 million, would be increased by $150 million for the additional work.

1965 July 1 - . Launch Vehicle: Saturn V.
Thermal problem with the Saturn V during ascent - . Nation: USA. Program: Apollo.
On the basis of information from the two Apollo spacecraft manufacturers, the Systems Engineering Division (SED) reported a possible thermal problem with the Saturn V during ascent:

On Saturns 501 and 502, the temperatures of the SM and the adapter would exceed design limits. (These limits were based on heating rates for 504, a heavier vehicle with a consequently cooler trajectory.)
And on 504, heating rates on the adapter would create an "unacceptable thermal environment" for the spacecraft within.
SED laid down study procedures to determine the best solution to this problem (either by modifying the spacecraft or the launch trajectory - or both).
1965 August 5 - . Launch Vehicle: Saturn V.
First ground test firing of Saturn S-IC stage - . Nation: USA. Program: Apollo.
The Saturn V's booster, the S-IC stage, made a "perfect" full-duration static firing by burning for the programmed 2.5 minutes at its full 33,360-kilonewton (7.5-million-lbs) thrust in a test conducted at MSFC. The test model demonstrated its steering capability on command from the blockhouse after 100 sec had elapsed; the firing consumed 2.133-million liters (537,000 gallons) of kerosene and liquid oxygen.

1965 August 15 - . Launch Vehicle: Saturn V.
First ground test firing of S-IVB stage - . Nation: USA. Program: Apollo. Class: Manned. Type: Manned space station.
1965 August 20 - . Launch Vehicle: Saturn V.
Apollo S-IVB static-fired simulating a lunar mission - . Nation: USA. Program: Apollo. Douglas Aircraft Company static-fired the S-IVB in a test at Sacramento, Calif., simulating the workload of a lunar mission. The stage was run for three minutes, shut down for half an hour, then reignited for almost six minutes..
1965 September - . Launch Vehicle: Saturn V.
Webb sees time as right to begin serious study of a Saturn V space station. - . Nation: USA. Related Persons: Webb. Spacecraft: LORL, Orbital Workshop, Skylab.
During several visits to MSC, NASA Administrator James E. Webb raised a number of technical and policy questions relating to programs and management practices. Webb seemed particularly concerned about the difficulty of getting the program offices at Headquarters and the Centers to take an active interest in NASA's potential influence in the national economy and world affairs. Additional Details: here....

1965 September 2-9 - . Launch Vehicle: Saturn V.
Abort feasibility for the AS-206 mission - . Nation: USA. Program: Apollo. Spacecraft: Apollo LM, LM Guidance. MSC's Flight Operations Division requested an investigation of the feasibility of performing an abort from an inoperative S-IVB booster on the AS-206 unmanned LEM mission..
1965 December 8 - . Launch Vehicle: Saturn V.
Apollo J-2 engine captive-fired for 388 sec - . Nation: USA. Program: Apollo.
An 889-kilonewton (200,000-lb) thrust J-2 engine was captive-fired for 388 sec on a new test stand at MSFC. The J-2 engine would be used to power the Saturn S-IVB stage for the Saturn V. Ten tests of the liquid hydrogen-liquid oxygen powered rocket engine had been conducted at MSFC since the J-2 engine test facility was put into use in August 1965.

1965 December 15 - . Launch Vehicle: Saturn V.
Apollo CSM ultimate static testing began - . Nation: USA. Program: Apollo. Flight: Apollo 204. Spacecraft: Apollo CSM, CSM Block I. CSM ultimate static testing began. A failure occurred at 140 percent of the limit load test which simulated the end of the first-stage Saturn V boost.. Additional Details: here....
1965 December 17 - . Launch Vehicle: Saturn V.
Proposal rejected that the Development Flight Instrumentation (DFI) on Apollo LEM-3 be deleted - . Nation: USA. Program: Apollo. Flight: Apollo 8, Apollo 9. Spacecraft: Apollo LM, LM Weight. The MSC Systems Development Branch rejected a proposal that the Development Flight Instrumentation (DFI) on LEM-3 be deleted for the following reasons:
LEM-3 would be the first full-weight LEM launched on a Saturn V vehicle. . Additional Details: here....
1965 December 19 - . Launch Vehicle: Saturn V.
Apollo Spacecraft and S-II stage program evaluations completed - . Nation: USA. Program: Apollo.
Apollo Program Director Samuel C. Phillips informed J. L. Atwood, President of North American Aviation, Inc., that he and the team working with him in examining the Apollo Spacecraft and S-II stage programs had completed their task "in sufficient detail . . . to formulate reasonably accurate assessment of the current situation concerning these two programs." Phillips and a task force had started this study at North American November 22, 1965.

Phillips added: "I am definitely not satisfied with the progress and outlook of either program and am convinced that the right actions now can result in substantial improvement of position in both programs in the relatively near future.

"Inclosed are ten copies of the notes which we compiled on the basis of our visits. They include details not discussed in our briefing and are provided for your consideration and use.

"The conclusions expressed in our briefing and notes are critical. Even with due consideration of hopeful signs, I could not find a substantive basis for confidence in future performance. I believe that a task group drawn from NAA at large could rather quickly verify the substance of our conclusions, and might be useful to you in setting the course for improvements.

"The gravity of the situation compels me to ask that you let me know, by the end of January if possible, the actions you propose to take. . . ."

1965 December - . Launch Vehicle: Saturn V.
Apollo LEM contract renegotiated - . Nation: USA. Program: Apollo. Spacecraft: Apollo LM.
MSC and Grumman completed negotiations to convert the LEM contract from cost-plus-fixed-fee to cost- plus-incentive fee. In addition to schedule and performance incentives, bonus points would be awarded for cost control during FY 66 and FY 67. Four LEMs were also added to the program. LEM mockup-3 would be used as the KSC verification vehicle; LEM test article-2 and LEM test article-10 (refurbished vehicles) would be used in the first two flights of the Saturn V launch vehicle.

A total of 167 contract change authorizations (CCAs) to the Grumman contract had been issued by December 31. Negotiation of the proposal for the conversion to a cost-plus-incentive-fee included all CCAs through No. 162, and CCA amendments dated before December 9. Proposals for CCAs 163167 were in process and would be submitted according to contract change procedures.

1966 January 6-13 - . Launch Vehicle: Saturn V.
Apollo Block I SPS engine tested to 600 seconds - . Nation: USA. Program: Apollo.
The 500-second limitation for the Block I service propulsion system SPS engine qualification program was increased to 600 seconds for the last three altitude qualification tests. The spacecraft 020 SPS mission duty cycle required a 310-second burn and a 205-second burn. Discussions with Systems Engineering Division indicated that the long SPS burns were needed to support a full-duration S-IVB mission and there was little likelihood the requirement could be modified. The Block II engine delivery schedules prohibited obtaining a Block II engine in time to support spacecraft 020.

1966 March 23 - . Launch Vehicle: Saturn V.
NASA released the first AAP schedule. It envisioned 26 Saturn IB and 19 Saturn V AAP launches. - . Nation: USA. Program: Skylab. Spacecraft: Orbital Workshop, Skylab.
Among these would be three 'S-IVB/Spent-Stage Experiment Support Modules' (i.e., 'wet' Workshops), three Saturn V-boosted orbital laboratories, and four Apollo telescope mounts. The initial AAP launch was slated for April 1968. The schedule was predicated upon non-interference with the basic Apollo lunar landing program, minimum modifications to basic Apollo hardware, and compatibility with existing Apollo launch vehicles.

1966 May 25 - . Launch Vehicle: Saturn V.
First full-scale Apollo Saturn V launch vehicle rolled out - . Nation: USA. Program: Apollo.
AS-500-F, the Pathfinder first full-scale Apollo Saturn V launch vehicle and spacecraft combination, was rolled out from Kennedy Space Center's Vehicle Assembly Building to the launch pad, for use in verifying launch facilities, training crews, and developing test procedures. The 111-meter, 227,000-kilogram vehicle was moved by a diesel-powered steel-link-tread crawler-transporter exactly five years after President John F. Kennedy asked the United States to commit itself to a manned lunar landing within the decade. Meanwhile, schedule for Saturn V threatened by continued problems in development of S-II stage (inability to get sustained 350-second burns without instrumentation failures, shutoffs, minor explosions).

1966 June 2 - . Launch Vehicle: Saturn V.
Development responsibility for the Apollo S027 X-ray Astronomy experiment - . Nation: USA. Program: Apollo.
Headquarters informed MSC that MSFC had been assigned development responsibility for the S027 X-ray Astronomy experiment for integration with the Saturn S-IVB/instrument unit. Should development be found not feasible, a modified version of the equipment was planned. MSC was requested to study:

the practicality of modifying the equipment to perform the scientific objectives and
the feasibility of integrating the modified experiment hardware in a Block II SM on an early Apollo Applications flight.
Study results were requested no later than July 1, 1966, including cost, schedule, and technical data.
1966 July 13 - . Launch Vehicle: Saturn V.
Apollo mission discontinuity leading to the lunar landing - . Nation: USA. Related Persons: Kraft, Shea. Program: Apollo. Flight: Apollo 204, Apollo 7. Spacecraft: Gemini.
MSC Director of Flight Crew Operations Donald K. Slayton and Director of Flight Operations Christopher C. Kraft, Jr., told ASPO Manager Joseph F. Shea: "A comprehensive examination of the Apollo missions leading to the lunar landing indicates that there is a considerable discontinuity between missions AS-205 and AS-207/208". Additional Details: here....

1966 August 3 - . Launch Vehicle: Saturn V.
Study of the visibility of the S-IVB/SLA from the left-hand couch in the Apollo command module - . Nation: USA. Program: Apollo. Spacecraft: Apollo LM, CSM Cockpit.
MSC requested LaRC to study the visibility of the S-IVB/SLA combination from the left-hand couch in the command module with the couch in the docked position. (Two positions could be attained, one of them a docking and rendezvous position that moved the seat into a better viewing area from the left-hand window.) LM and CM mockups were already at Langley from the CM-active moving-base docking simulation conducted May-July 1965.

The request was initiated because the flight crew had to rely on an out- the-window reference of the S-IVB/SLA to verify separation of the LM/CSM combination from the S-IVB/SLA. The question arose as to whether the out-the-window reference was sufficient or whether an electromechanical device with a panel readout in the CM was required to verify separation.

1966 August 8 - . Launch Vehicle: Saturn V.
Manual control simulation of the Saturn V upper stages with Apollo - . Nation: USA. Program: Apollo.
MSC requested Ames Research Center to conduct a manual control simulation of the Saturn V upper stages with displays identical to those planned in the spacecraft. On August 5, Brent Creer and Gordon Hardy of Ames had met with representatives from ASPO, Guidance and Control Division, and Flight Crew Operations Directorate to discuss implementation of a modified Ames simulation which would determine feasibility of manual control from first stage burnout, using existing spacecraft displays and control interfaces. Simulations at Ames in 1965 had indicated that the Saturn V could be manually flown into orbit within dispersions of 914 meters in altitude, and 0.1 degree in flight path angle. Additional Details: here....

1966 October 21 - . Launch Vehicle: Saturn V.
Langley Apollo Visibility Study - . Nation: USA. Program: Apollo. Spacecraft: Apollo CSM.
Langley Research Center informed MSC that the Apollo Visibility Study requested by MSC would be conducted. Langley mockups could be used along with an SLA panel to be provided by MSC from Tulsa North American. The proposed study would be semistatic, with the astronaut seated in the existing CM mockup and viewing the S-IVB/SLA mockup. The positions of the mockups would be varied manually by repositioning the mockup dollies, and the astronaut would judge the separation distance and alignment attitude. The study was expected to start at the end of October or early November and last two or three weeks.

1966 December 5 - . Launch Vehicle: Saturn V.
Evaluation of recovery areas for Saturn V Apollo missions - . Nation: USA. Program: Apollo. Flight: Apollo 8. In response to a request from Apollo Program Director Samuel C. Phillips on November 21, MSC reported its evaluation of Atlantic versus Pacific Ocean prime recovery areas for all Saturn V Apollo missions. . Additional Details: here....
1966 December 6 - . Launch Vehicle: Saturn V.
Study of visibility from the Apollo CSM during extraction of the LM from the S-IVB stage - . Nation: USA. Program: Apollo. Spacecraft: Apollo LM, CSM Cockpit, LM Crew Station.
Langley Research Center reported on its November study of visibility from the CSM during extraction of the LM from the S-IVB stage. The study had been made in support of the AS-207/208A mission, with assistance of MSC and North American Aviation personnel, to

determine if the CSM pilot could detect the signal indicating that the CSM had detached from the S-IVB,
determine if he could recognize a misalignment between the CSM/LM combination and the S-IVB during withdrawal, and
investigate simple aid techniques to make the pilot's task easier.
Results indicated that
LM docking did not provide adequate indication of detachment of the LM from the S-IVB, but
in misalignment tests subjects could recognize errors as small as two to three degrees in yaw and five to seven centimeters in lateral translation except when the CSM/LM was yawed right and translated left relative to the S-IVB.
The configuration of the model used prevented studying pitch, roll, or vertical translation misalignments.
1966 December 22 - . Launch Vehicle: Saturn V.
S-IVB stage venting dispute - . Nation: USA. Program: Apollo.
Lewis L. McNair, MSFC Chairman of the Flight Mechanics Panel, told Calvin H. Perrine, Jr., MSC, that the Guidance and Performance Sub-Panel had been unable to reach an agreement on venting the liquid-oxygen (LOX) tank of the Saturn V S-IVB stage during earth parking orbit. McNair pointed out that MSFC did not want a programmed LOX vent and that MSC did. He added that the issue must be resolved in order to finalize the AS-501 attitude maneuver and venting timeline.

1966 December 22 - . Launch Vehicle: Saturn V.
Crew selection for the second and third manned Apollo missions - . Nation: USA. Related Persons: Anders. Program: Apollo. Flight: Apollo 7, Apollo 8. Spacecraft: Apollo LM. NASA announced crew selection for the second and third manned Apollo missions. . Additional Details: here....
1967 January 10 - . Launch Vehicle: Saturn V.
Use of "direct translunar injection" for Apollo - . Nation: USA. Program: Apollo.
Apollo Program Director Samuel C. Phillips told NASA Associate Administrator for Manned Space Flight George E. Mueller that studies had been completed on the use of "direct translunar injection" (launch directly into a trajectory to the moon) as a mode of operation for lunar landing missions. The principal advantages would be potential payload increases and elimination of the S-IVB stage restart requirement. The disadvantage was that there would be no usable launch windows for about half of each year and a reduced number of windows for the remainder of the year. Phillips was confident the launch vehicle would have adequate payload capability, since Saturn V performance continued to exceed spacecraft requirements. Confidence in successful S-IVB restarts was also high. For the lunar missions, therefore, direct launch was considered as a fall-back position and the effort was concentrating on the parking orbit mode.

1967 January 20 - . Launch Vehicle: Saturn V.
Apollo S-IVB stage for Saturn launch vehicle 503 exploded - . Nation: USA. Program: Apollo.
The Saturn 503 S-IVB stage exploded and was destroyed at the Douglas Sacramento, Calif., Test Facility at 4:25 p.m. PST during a countdown. The exercise had progressed to 10 seconds before simulated launch (about 8 minutes before S-IVB ignition) when the explosion occurred. Additional Details: here....

1967 January 26 - . Launch Vehicle: Saturn V.
Findings of the S-IVB Accident Investigation Board supplemented - . Nation: USA. Program: Apollo. Flight: Apollo 204.
Apollo Program Director Samuel C. Phillips sent a message to the manned space flight Centers indicating that he wanted to supplement the findings of the S-IVB Accident Investigation Board with a review by the Crew Safety Panel of the possible impact on manned Apollo flights. Additional Details: here....

1967 February 7 - . Launch Vehicle: Saturn V.
Study at Langley to familiarize flight crews with Apollo CM active docking - . Nation: USA. Program: Apollo. Spacecraft: Apollo LM, CSM Block II, LM Crew Station.
MSC Director Robert R. Gilruth asked LaRC Director Floyd Thompson to conduct a study at Langley to familiarize flight crews with CM active docking and to explore problems in CM recontact with the LM and also LM withdrawal. MSC would provide astronaut and pilot-engineer support for the study. Apollo Block II missions called for CM active docking with the LM and withdrawal of the LM from the S-IVB stage, requiring development of optimum techniques and procedures to ensure crew safety and to minimize propellant utilization. LM withdrawal was a critical area because of clearances, marginal flight crew visibility, and mission constraints. Previous simulations at LaRC indicated the possibility of using the Rendezvous Docking Simulator.

1967 February 10 - . Launch Vehicle: Saturn V.
Apollo S-IVB stage explosion accident cause - . Nation: USA. Program: Apollo.
The Board of Inquiry into the January 20 S-IVB-503 explosion at the Douglas Sacramento Test Facility identified the probable cause as the failure of a pressure vessel made with titanium-alloy parent-metal fusion welded with commercially pure titanium. The combination, which was in violation of specifications, formed a titanium hydride intermetallic that induced embrittling in the weld nugget, thus significantly degrading the capabilities of a weldment to withstand sustained pressure loads. The Board recommended pressure limitations for titanium-alloy pressure vessels.

1967 March 7 - . Launch Vehicle: Saturn V.
Impact of the Apollo 204 accident on schedules - . Nation: USA. Program: Apollo. Flight: Apollo 204.
During a House Committee on Science and Astronautics hearing on NASA's FY 1968 authorization, NASA Administrator James E. Webb replied to questions by Congressmen John W. Wydler, Edward J. Gurney, and Emilio Q. Daddario about the impact of the Apollo 204 accident on schedules for accomplishing the lunar landing. Additional Details: here....

1967 March 8 - . Launch Vehicle: Saturn V.
Saturn V translunar payload 44,500 kilograms - . Nation: USA. Related Persons: Mueller. Program: Apollo. Spacecraft: Apollo LM, LM Weight.
NASA Associate Administrator for Manned Space Flight George E. Mueller stated that the February completion of MSFC studies of the Saturn V launch vehicle's payload and structural capability would permit an official revision of the payload from 43,100 kilograms to 44,500 kilograms; the CM weight would be revised from 5,000 to 5,400 kilograms; and the LM from 13,600 to 14,500.

1967 March 15 - . Launch Vehicle: Saturn V.
Rendezvous with S-IVB stage primary objective of Apollo 7 - . Nation: USA. Related Persons: Kraft. Program: Apollo. Flight: Apollo 7. Spacecraft: Apollo CSM. MSC Director of Flight Crew Operations Donald K. Slayton requested that a rendezvous of the CSM with its launch vehicle S-IVB stage be a primary objective of the Apollo 2 mission.. Additional Details: here....
1967 April 1 - . Launch Vehicle: Saturn V.
Replacement of the Apollo service module 017 oxidizer tank - . Nation: USA. Program: Apollo. Spacecraft: Apollo CSM, CSM Block I. In reply to a request from NASA Hq., CSM Manager Kenneth S. Kleinknecht told Apollo Program Director Samuel C. Phillips that replacement of the service module 017 oxidizer tank was based on a double repair weld of the method 2 kind in that tank. . Additional Details: here....
1967 April 14 - . Launch Vehicle: Saturn V.
Apollo pressure vessel tests returned to normal channels - . Nation: USA. Program: Apollo.
NASA Hq. informed the Directors of the manned space flight Centers that responsibility for approval of pressure vessel tests was being returned to normal Center management channels. Because of the failure of the 503 launch vehicle S-IVB stage and other pressure vessel problems, testing had been restricted by the office of the Apollo Program Director. The Program Director now returned to the Center Directors "responsibility for approving pressurization tests of pressure vessels in spacecraft modules, launch vehicle stages, and ground support equipment within their Apollo program responsibilities."

1967 April 17 - . Launch Vehicle: Saturn V.
Requirements of the Apollo flight program before the first lunar landing mission - . Nation: USA. Related Persons: Kraft. Program: Apollo. Flight: Apollo 7. Spacecraft: Apollo LM. A meeting at MSC considered requirements of the Apollo flight program before the first lunar landing mission. . Additional Details: here....
1967 April 18 - . Launch Vehicle: Saturn V.
Plans for launching Apollo-Saturn space vehicles - . Nation: USA. Program: Apollo.
NASA Apollo Program Director Samuel C. Phillips signed a directive defining the requirements, responsibilities, and inter-Center coordination necessary for development, control, and execution of test and checkout plans and procedures for preparing and launching Apollo-Saturn space vehicles at KSC.

1967 May 5 - . Launch Vehicle: Saturn V.
Minimum restart capability for Saturn S-IVB stage - . Nation: USA. Program: Apollo. Spacecraft: Apollo CSM.
After review of operational considerations for a minimum restart capability in the Saturn launch vehicle's S IVB stage, MSC's Director of Flight Operations reported to NASA Hq. that an 80-minute restart capability was believed the best compromise for the early lunar missions, "for the primary reason of providing sufficient time for ground support in verifying navigation, and flight crew checkout of CSM and S-IVB systems prior to TLI (translunar injection), while providing for two injection opportunities in both the Atlantic and Pacific Oceans (second and third revolutions). For later missions, consideration should be given to the hardware implications of providing a restart capability with minimum (zero) restrictions, so that advantage may be taken of confidence in onboard systems to gain additional payload."

1967 May 19 - . Launch Vehicle: Saturn V.
Apollo CSM Block II spacecraft vibration program begun - . Nation: USA. Program: Apollo. Spacecraft: Apollo CSM, CSM Block II.
A Block II spacecraft vibration program was begun to provide confidence in CSM integrity and qualify the hardware interconnecting the subsystems within the spacecraft. A test at MSC was to simulate the vibration environment of max-q flight conditions. The test article was to be a Block II CSM. A spacecraft-LM adapter, an instrumentation unit, and an S-IVB stage forward area simulation would also be used.

1967 June 8 - . Launch Vehicle: Saturn V.
Rendezvous with the S-IVB stage by the first manned Apollo - . Nation: USA. Program: Apollo. Spacecraft: Apollo CSM.
Apollo Program Director Samuel C. Phillips, in a message to ASPO Manager George M. Low, spoke of a June 2 agreement to include a CSM active rendezvous with the Saturn S-IVB stage of the launch vehicle in the mission profile of the first manned Apollo mission. Phillips said that it should be recognized that such a rendezvous would not be a primary objective for the first manned mission and that the decision should be reviewed if any related problem that would complicate mission preparations were identified.

1967 June 20 - . Launch Vehicle: Saturn V.
Apollo spacecraft mated to Saturn V for Apollo 4 - . Nation: USA. Program: Apollo. Apollo spacecraft 017 was mechanically mated to its Saturn V launch vehicle at KSC in preparation for the Apollo 4 (AS-501) unmanned mission, scheduled for the third quarter of 1967..
1967 July 26 - . Launch Vehicle: Saturn V.
NASA awarded The Boeing Company a contract for long-lead-time materials (such as propellant ducts and fuel tank components) for two additional Saturn V's. - . Nation: USA. Spacecraft: Orbital Workshop, Skylab. This contract marked the first Saturn V procurement in support of Apollo Applications Program..
1967 August 1 - . Launch Vehicle: Saturn V.
Rocketdyne to build injectors for the Apollo lascent engine - . Nation: USA. Program: Apollo. Spacecraft: Apollo LM, LM Ascent Propulsion.
Rocketdyne Division of North American Aviation was selected for negotiation of a contract for the design, development, qualification, and delivery of four production models of an injector for the lunar module ascent engine. The project would serve as a backup to the injector program already being conducted by Bell Aerospace Corp. under subcontract to Grumman. The ascent engine was considered to be the most critical engine in the Apollo-Saturn vehicle. No backup mode of operation remained if the ascent engine failed.

1967 August 11 - . Launch Vehicle: Saturn V.
Review of the content of the Apollo program to determine alternatives for budget decisions - . Nation: USA. Program: Apollo. Spacecraft: Apollo Lunar Landing.
Apollo Program Director Samuel C. Phillips was appointed Chairman of a NASA task group, reporting to Administrator James E. Webb, Deputy Administrator Robert C. Seamans, Jr., and Associate Administrator for Manned Space Flight George E. Mueller. The group was chartered to review the content of the Apollo program in order to determine alternatives necessary for programming and budget planning decisions. It would inquire into and report on all aspects of the Apollo program necessary to provide a base of accurate data and information to support decisions on FY 1968 expenditure control and FY 1969 budget planning. Specifically, the group was requested to identify planned activities that could be eliminated if the Apollo program were to be terminated with the manned lunar landing. The group was also requested to determine the effect of placing a hold order on production of Saturn V vehicles 512 through 515 and to develop the cost estimates resulting from these actions as well as other tangible alternatives.

1967 October 8 - . Launch Vehicle: Saturn V.
Abort of Apollo in the near-pad region would result in land impact - . Nation: USA. Program: Apollo.
Because of wind conditions, an abort of the Apollo spacecraft from a Saturn V in the near-pad region would result in land impact. To ensure the maximum potential safe recovery of the crew during a near-pad abort, certain forms of preparation within the abort area were being considered. Tests were being prepared at MSC and KSC to determine the most favorable soil condition for spacecraft landing. The capability of the spacecraft to sustain a land impact was also being investigated by MSC.

1967 November 9 - . 12:00 GMT - . Launch Site: Cape Canaveral. Launch Complex: Cape Canaveral LC39A. Launch Platform: LUT1. Launch Vehicle: Saturn V.
Apollo 4 - . Payload: Apollo CSM 017 / LTA-10R / S-IVB-501. Mass: 36,656 kg (80,812 lb). Nation: USA. Agency: NASA Houston. Program: Apollo. Class: Moon. Type: Manned lunar spacecraft. Spacecraft: Apollo CSM. Duration: 2.35 days. Decay Date: 1967-11-09 . USAF Sat Cat: 3032 . COSPAR: 1967-113A. Apogee: 371 km (230 mi). Perigee: 370 km (220 mi). Inclination: 32.7000 deg. Period: 91.90 min.
Apollo 4 (AS-501) was launched in the first all-up test of the Saturn V launch vehicle and also in a test of the CM heatshield. The Saturn V, used for the first time, carried a lunar module test article (LTA-10R) and a Block I command and service module (CSM 017) into orbit from KSC Launch Complex 39, Pad A, lifting off at 7:00:01 a.m. EST - one second later than planned. The launch was also the first use of Complex 39. The spacecraft landed 8 hours 37 minutes later in the primary recovery area in the Pacific Ocean, near Hawaii, about 14 kilometers from the planned point (30.06 N 172.32 W). CM, apex heatshield, and one main parachute were recovered by the carrier U.S.S. Bennington

Main objectives of the mission were to demonstrate the structural and thermal integrity of the space vehicle and to verify adequacy of the Block II heatshield design for entry at lunar return conditions. These objectives were accomplished.

The S-IC stage cutoff occurred 2 minutes 30 seconds into the flight at an altitude of about 63 kilometers. The S-II stage ignition occurred at 2 minutes 32 seconds and the burn lasted 6 minutes 7 seconds, followed by the S-IVB stage ignition and burn of 2 minutes 25 seconds. This series of launch vehicle operations placed the S-IVB and spacecraft combination in an earth parking orbit with an apogee of about 187 kilometers and a perigee of 182 kilometers. After two orbits, which required about three hours, the S-IVB stage was reignited to place the spacecraft in a simulated lunar trajectory. This burn lasted five minutes. Some 10 minutes after completion of the S-IVB burn, the spacecraft and S-IVB stage were separated, and less than 2 minutes later the service propulsion subsystem was fired to raise the apogee. The spacecraft was placed in an attitude with the thickest side of the CM heatshield away from the solar vector. During this four-and-one-half-hour cold-soak period, the spacecraft coasted to its highest apogee - 18,256.3 kilometers. A 70 mm still camera photographed the earth's surface every 10.6 seconds, taking 715 good-quality, high-resolution pictures.

About 8 hours 11 minutes after liftoff the service propulsion system was again ignited to increase the spacecraft inertial velocity and to simulate entry from a translunar mission. This burn lasted four and one half minutes. The planned entry velocity was 10.61 kilometers per second, while the actual velocity achieved was 10.70.

Recovery time of 2 hours 28 minutes was longer than anticipated, with the cause listed as sea conditions - 2.4-meter swells.

1967 November 15 - . Launch Vehicle: Saturn V.
Payloads for Apollo AS-503 - . Nation: USA. Program: Apollo. Flight: Apollo 8. Spacecraft: Apollo LM.
MSC informed MSFC that it would provide the following payload flight hardware for the AS-503/BP-30 flight test: boilerplate 30 (BP-30, already at MSFC); spacecraft-LM adapter 101 and launch escape system (SLA-101/LES) jettisonable mass simulation; and lunar module test article B (LTA-B, already at MSFC). MSC had no mission requirements but recommended that any restart test requirements for the Saturn S-IVB stage be carried out on this mission to simplify requirements for the first manned Saturn V mission.

1967 December 1 - . Launch Vehicle: Saturn V.
Plans resulting from Apollo 4 mission - . Nation: USA. Program: Apollo. Flight: Apollo 8.
NASA Hq. announced that, as concurred in by the Center Apollo Program Managers, the following decisions, based on the results of the Apollo 4 mission, were firmly established:

CSM 020 would be flown on the Apollo 6 mission.
Boilerplate 30 was assigned to the AS-503 unmanned mission.
If Apollo 6 was successful, AS-503 would be flown as the first Saturn V manned mission.
1967 December 14 - . Launch Vehicle: Saturn V.
Apollo schedule decisions - . Nation: USA. Related Persons: Phillips, Samuel. Program: Apollo. Spacecraft: Apollo LM.
Apollo Program Director Samuel C. Phillips wrote the manned space flight Centers of Apollo schedule decisions. In a September 20 meeting at MSC to review the Apollo test flight program, MSC had proposed a primary test flight plan including

the addition of a second unmanned LM flight,
addition of a third unmanned Saturn V flight, and
addition of a new' primary mission, a lunar orbital mission.
Phillips now wrote that decisions had been made to accommodate MSC's first two proposals into the mainline Apollo flight mission assignment. In addition, the proposal for the lunar orbital mission would be included in the Apollo flight mission assignments as an alternate to a landing mission.
1968 January 9 - . Launch Vehicle: Saturn V.
Key Apollo program decisions required to certify the Apollo system design summarized - . Nation: USA. Program: Apollo. Flight: Apollo 7, Apollo 8. Spacecraft: Apollo LM.
George E. Mueller, NASA OMSF, in a letter to MSC Director Robert R. Gilruth, summarized a number of key Apollo program decisions required in order to emphasize the urgency of priority action in preparations necessary to certify the Apollo system design for manned flight. Additional Details: here....

1968 April 4 - . 12:00 GMT - . Launch Site: Cape Canaveral. Launch Complex: Cape Canaveral LC39A. Launch Platform: LUT2. Launch Vehicle: Saturn V.
Apollo 6 - . Payload: Apollo CM 020/ SM 014 / Apollo LTA-2R / S-IVB 502. Mass: 36,806 kg (81,143 lb). Nation: USA. Agency: NASA Houston. Program: Apollo. Class: Moon. Type: Manned lunar spacecraft. Spacecraft: Apollo CSM. Duration: 2.43 days. Decay Date: 1968-04-04 . USAF Sat Cat: 3170 . COSPAR: 1968-025A. Apogee: 184 km (114 mi). Perigee: 183 km (113 mi). Inclination: 32.5000 deg. Period: 88.20 min.
Apollo 6 (AS-502) was launched from Complex 39A at Kennedy Space Center. The space vehicle consisted of a Saturn V launch vehicle with an unmanned, modified Block I command and service module (CSM 020) and a lunar module test article (LTA-2R).

Liftoff at 7:00 a.m. EST was normal but, during the first-stage (S-IC) boost phase, oscillations and abrupt measurement changes were observed. During the second-stage (S-II) boost phase, two of the J-2 engines shut down early and the remaining three were extended approximately one minute to compensate. The third stage (S-IVB) firing was also longer than planned and at termination of thrust the orbit was 177.7 x 362.9 kilometers rather than the 160.9-kilometer near-circular orbit planned. The attempt to reignite the S-IVB engine for the translunar injection was unsuccessful. Reentry speed was 10 kilometers per second rather than the planned 11.1, and the spacecraft landed 90.7 kilometers uprange of the targeted landing point.

The most significant spacecraft anomaly occurred at about 2 minutes 13 seconds after liftoff, when abrupt changes were indicated by strain, vibration, and acceleration measurements in the S-IVB, instrument unit, adapter, lunar module test article, and CSM. Apparently oscillations induced by the launch vehicle exceeded the spacecraft design criteria.

The second-stage (S-II) burn was normal until about 4 minutes 38 seconds after liftoff; then difficulties were recorded. Engine 2 cutoff was recorded about 6 minutes 53 seconds into the flight and engine 3 cutoff less than 3 seconds later. The remaining second-stage engines shut down at 9 minutes 36 seconds - 58 seconds later than planned.

The S-IVB engine during its first burn, which was normal, operated 29 seconds longer than programmed. After two revolutions in a parking orbit, during which the systems were checked, operational tests performed, and several attitude maneuvers made, preparations were completed for the S-IVB engine restart. The firing was scheduled to occur on the Cape Kennedy pass at the end of the second revolution, but could not be accomplished. A ground command was sent to the CSM to carry out a planned alternate mission, and the CSM separated from the S-IVB stage.

A service propulsion system (SPS) engine firing sequence resulted in a 442-second burn and an accompanying free-return orbit of 22,259.1 x 33.3 kilometers. Since the SPS was used to attain the desired high apogee, there was insufficient propellant left to gain the high-velocity increase desired for the entry. For this reason, a complete firing sequence was performed except that the thrust was inhibited.

Parachute deployment was normal and the spacecraft landed about 9 hours 50 minutes after liftoff, in the mid-Pacific, 90.7 kilometers uprange from the predicted landing area (27.40 N 157.59 W). A normal retrieval was made by the U.S.S. Okinawa, with waves of 2.1 to 2.4 meters.

The spacecraft was in good condition, including the unified crew hatch, flown for the first time. Charring of the thermal protection was about the same as that experienced on the Apollo 4 spacecraft (CM 017).

Of the five primary objectives, three - demonstrating separation of launch vehicle stages, performance of the emergency detection system (EDS) in a close-loop mode, and mission support facilities and operations - were achieved. Only partially achieved were the objectives of confirming structure and thermal integrity, compatibility of launch vehicle and spacecraft, and launch loads and dynamic characteristics; and of verifying operation of launch vehicle propulsion, guidance and control, and electrical systems. Apollo 6, therefore, was officially judged in December as "not a success in accordance with . . . NASA mission objectives."

1968 April 23 - . Launch Vehicle: Saturn V.
Task team of all participants in the dynamic analysis of the Saturn V and boost environment - . Nation: USA. Program: Apollo. Spacecraft: Apollo LM, CSM Block II, LM ECS.
ASPO Manager George M. Low requested Joseph N. Kotanchik to establish a task team to pull together all participants in the dynamic analysis of the Saturn V and boost environment. He suggested that Donald C. Wade should lead the effort and that he should work with George Jeffs of North American Rockwell, Tom Kelly of Grumman and Wayne Klopfenstein of Boeing, and that Lee James of MSFC could be contacted for any desired support or coordination. The team would define the allowable oscillations at the interface of the spacecraft-LM adapter with the instrument unit for the existing Block II configuration, possible changes in the hardware to detune the CSM and the LM, and the combined effects of pogo and the S-IC single-engine-out case. Low also said he was establishing a task team under Richard Colonna to define a test program related to the same problem area and felt that Wade and Colonna would want to work together.

1968 April 27 - . Launch Vehicle: Saturn V.
Preparation of third Saturn V for an Apollo manned mission - . Nation: USA. Program: Apollo. NASA Administrator James E. Webb approved plans to proceed with preparation of the third Saturn V space vehicle for a manned mission in the fourth quarter of 1968. . Additional Details: here....
1968 May 25 - . Launch Vehicle: Saturn V.
Effects of launch vehicle "pogo" vibrations - on Apollo spacecraft studied - . Nation: USA. Program: Apollo. Spacecraft: Apollo LM, CSM Parachute. ASPO Manager George M. Low informed Apollo Program Director Samuel C. Phillips of recent MSC work on the effects of launch vehicle-induced oscillations - i.e., "pogo" vibrations - on the spacecraft and its subsystems. . Additional Details: here....
1968 July 5 - . Launch Vehicle: Saturn V.
Apollo spacecraft to withstand bending loads due to a failure of engines on the Saturn V booster - . Nation: USA. Program: Apollo.
ASPO Manager George M. Low asked Aaron Cohen, one of his chief technical assistants, to investigate the ability of the Apollo spacecraft to withstand bending loads imposed by a failure of one or more engines on the Saturn V launch vehicle (as well as actual loads that would be imposed on the spacecraft). Additional Details: here....

1968 July 23 - . Launch Vehicle: Saturn V.
New Saturn V payload at translunar injection of 46,040 kilograms established - . Nation: USA. Program: Apollo.
Prompted by a request from MSC to increase the Saturn V's performance to 46,070 kilograms for lunar missions, Samuel C. Phillips sought to strike a balance between spacecraft and launch vehicle weight-performance demands. He established as a new payload interface definition at translunar injection a payload of 46,040 kilograms. Should the vehicle per se be incapable of achieving this figure, said Phillips, he would relax certain flight constraints to achieve the best possible balance between the space vehicle and the specific mission to be flown. But he implored both ASPO Manager George M. Low and Lee B. James, Saturn V Program Manager at MSFC, to work toward this balance between spacecraft and launch vehicle and to avoid any hardware changes in the Saturn V solely to meet the new payload interface weight.

1968 July 30 - . Launch Vehicle: Saturn V.
Plans for S-IVB and Apollo spacecraft separation and use of a slingshot trajectory toward the moon - . Nation: USA. Related Persons: Speer. Program: Apollo.
F. A. Speer, Mission Operations Manager at MSFC, advised NASA Hq. of plans for S-IVB and spacecraft separation and employment of a "slingshot" trajectory following insertion into the trajectory toward the moon. Residuals in the S-IVB, said Speer, could be used to place the stage in a trajectory that would avoid recontact with the spacecraft and impact on either the earth or the moon - with preclusion of spacecraft-launch vehicle collision as the most important priority.

1968 August 1 - . Launch Vehicle: Saturn V.
Following receipt of NASA direction to limit Saturn V production to Vehicle 515, MSFC began terminating production of engine hardware for the Apollo and Apollo Applications programs. - . Nation: USA. Program: Skylab. The action involved 27 H-1, eight F-1, and three J-2 rocket engines..
1968 August 7 - . Launch Vehicle: Saturn V.
George Low promotes idea of flying Apollo 8 as a lunar orbit mission without the Lunar Module - . Nation: USA. Related Persons: von Braun. Program: Apollo. Flight: Apollo 7, Apollo 8, Apollo 9. Spacecraft: Apollo CSM, Apollo LM, CSM Block II, LM Guidance, LM RCS.
On August 7, Low asked MSC's Director of Flight Operations Christopher C. Kraft, Jr., to look into the feasibility of a lunar orbit mission for Apollo 8 without carrying the LM. A mission with the LM looked as if it might slip until February or March 1969. The following day Low traveled to KSC for an AS-503 review, and from the work schedule it looked like a January 1969 launch. Additional Details: here....

1968 August 9 - . Launch Vehicle: Saturn V.
Senior Apollo porject management backs Apollo 8 lunar mission concept - . Nation: USA. Related Persons: Low, George, von Braun. Program: Apollo. Flight: Apollo 7, Apollo 8, Apollo 9. Spacecraft: Apollo CSM, Apollo LTA. August 9 was probably one of the busiest days in George Low's life; the activities of that and the following days enabled the United States to meet the "in this decade" goal.. Additional Details: here....
1968 August 10 - . Launch Vehicle: Saturn V.
North American not enthusiastic about plan to send Apollo 8 to moon. - . Nation: USA. Related Persons: Low, George. Program: Apollo. Flight: Apollo 7, Apollo 8. Spacecraft: Apollo CSM, Apollo LTA. More detailed reviews within NASA showed there were still no obvious insurmountable problems that might block the plan. However North American was not too receptive to the idea.. Additional Details: here....
1968 August 12 - . Launch Vehicle: Saturn V.
Apollo pogo structural testing quality surveillance defined - . Nation: USA. Related Persons: Grau. Program: Apollo.
Dieter Grau, Director of Quality and Reliability Assurance at MSFC, sent his Houston counterpart Martin Raines a memorandum of understanding covering exchanges of quality surveillance responsibility in support of pogo structural testing under way both in Huntsville, Ala., and at MSC. Testing was being conducted simultaneously at the Wyle Laboratories in Huntsville (under contract to North American Rockwell, primarily static loading and referred to as shell stability tests); and dynamic load testing at MSC (called the "short stack" dynamic tests). In effect, each Center assumed the task of overseeing the complete test article (spacecraft, instrument unit, and S-IVB forward skirt) being tested at its own location.

1968 August 12 - . Launch Vehicle: Saturn V.
Apollo 8 lunar mission scheduled for December 20. - . Nation: USA. Related Persons: Low, George. Program: Apollo. Flight: Apollo 8. Spacecraft: Apollo CSM, Apollo LTA.
On August 12 Kraft informed Low that December 20 was the day if they wanted to launch in daylight. With everyone agreeing to a daylight launch, the launch was planned for December 1 with a "built-in hold" until the 20th, which would have the effect of giving assurance of meeting the schedule. LTA (LM test article)-B was considered as a substitute; it had been through a dynamic test vehicle program, and all except Kotanchik agreed this would be a good substitute. Grumman suggested LTA-4 but Low decided on LTA-B.

1968 August 13 - . Launch Vehicle: Saturn V.
Borman crew selected for Apollo 8 lunar mission. - . Nation: USA. Related Persons: Borman, Low, George. Program: Apollo. Flight: Apollo 8, Apollo 9. Spacecraft: Apollo CSM.
Kleinknecht had concluded his CSM 103-106 configuration study by August 13 and determined the high-gain antenna was the most critical item. Kraft was still "GO" and said December 20-26 (except December 25) offered best launch times; he had also looked at January launch possibilities. Slayton had decided to assign the 104 crew to the mission. He had talked to crew commander Frank Borman and Borman was interested.

1968 August 14 - . Launch Vehicle: Saturn V.
During a key meeting of Apollo senior figures - top NASA management first approached regarding an Apollo 8 lunar mission in December - reaction: negative. - . Nation: USA. Related Persons: Debus, Low, George, von Braun. Program: Apollo. Flight: Apollo 8. Spacecraft: Apollo CSM.
Participants in the August 14 meeting in Washington were Low, Gilruth, Kraft, and Slayton from MSC; von Braun, James, and Richard from MSFC; Debus and Petrone from KSC; and Deputy Administrator Thomas Paine, William Schneider, Julian Bowman, Phillips, and Hage from NASA Hq. Low reviewed the spacecraft aspects; Kraft, flight operations; and Slayton, flight crew support. MSFC had agreed on the LTA-B as the substitute and were still ready to go; and KSC said they would be ready by December 6. Additional Details: here....

1968 August 15 - . Launch Vehicle: Saturn V.
Webb briefed on Apollo 8 lunar mission concept. - . Nation: USA. Related Persons: Low, George, Paine, Phillips, Samuel, Webb. Program: Apollo. Flight: Apollo 7, Apollo 8. Spacecraft: Apollo CSM.
Phillips and Paine discussed the plan with Webb in Vienna. Webb wanted to think about it, and requested further information by diplomatic carrier. That same day Phillips called Low and informed him that Mueller had agreed to the plan with the provisions that no full announcement would be made until after the Apollo 7 flight; that it could be announced that 503 would be manned and possible missions were being studied; and that an internal document could be prepared for a planned lunar orbit for December.

1968 August 17 - . Launch Vehicle: Saturn V.
Further development of a pogo sensor for the Apollo Apollo CSM halted - . Nation: USA. Program: Apollo. Spacecraft: Apollo CSM. ASPO Manager George M. Low wrote Program Director Samuel C. Phillips seeking to halt further development of a pogo sensor for the CSM. . Additional Details: here....
1968 August 17 - . Launch Vehicle: Saturn V.
Webb approves Apollo 8 lunar orbit mission for December - but no public announcement until after a successful Apollo 7 flight. - . Nation: USA. Related Persons: Low, George, Webb. Program: Apollo. Flight: Apollo 7, Apollo 8, Apollo 9. Spacecraft: Apollo CSM.
Phillips and Hage visited MSC, bringing the news that Webb had given clear-cut authority to prepare for a December 6 launch, but that they could not proceed with clearance for lunar orbit until after the Apollo 7 flight, which would be an earth-orbital mission with basic objectives of proving the CSM and Saturn V systems. Phillips said that Webb had been "shocked and fairly negative" when he talked to him about the plan on August 15. Subsequently, Paine and Phillips sent Webb a lengthy discourse on why the mission should be changed, and it was felt he would change his mind with a successful Apollo 7 mission.

1968 August 19 - . Launch Vehicle: Saturn V.
Changes in planning for Apollo flights - . Nation: USA. Related Persons: Anders, Borman, Lovell. Program: Apollo. Flight: Apollo 8. Spacecraft: Apollo LM, Apollo Lunar Landing, CSM SPS.
In a Mission Preparation Directive sent to the three manned space flight Centers, NASA Apollo Program Director Samuel C. Phillips stated that the following changes would be effected in planning and preparation for Apollo flights:

Apollo-Saturn 503
Assignment of Saturn V 503, CSM 103, and LM-3 to Mission D was canceled.
Saturn V 503 would be prepared to carry CSM 103 and LTA (LM test article)-B on a manned CSM-only mission to be designated the C prime mission.
The objectives and profile of the C prime mission would be developed to provide maximum gain consistent with standing flight safety requirements. Studies would be carried out and plans prepared so as to provide reasonable flexibility in establishing final mission objectives.
All planning and preparations for the C prime mission would proceed toward launch readiness on December 6, 1968.
Apollo-Saturn 504
Saturn V 504, CSM 104, and LM-3 were assigned to the D mission, scheduled for launch readiness no earlier than February 20, 1969. The crew assigned to the D mission would remain assigned to that mission. The crew assigned to the E mission (Frank Borman, James A. Lovell, Jr., and William Anders) would be reassigned to the C prime mission. Training and equipping the C prime crews and operational preparations would proceed as required to meet mission requirements and to meet the newly established flight readiness date.
Additional Details: here....
1968 August 26 - . Launch Vehicle: Saturn V.
Payload weight of 39.78 tonnes for Apollo AS-503 - . Nation: USA. Program: Apollo. Flight: Apollo 8. Spacecraft: Apollo LM, LM Weight.
ASPO Manager George M. Low asked Joseph N. Kotanchik, head of the Structures and Mechanics Division, to verify that all spacecraft load analyses and safety factors were compatible with the recently agreed-on payload weight of 39,780 kilograms for the AS-503 mission. Additional Details: here....

1968 August 27 - . Launch Vehicle: Saturn V.
Decision to use Apollo LTA-B as payload ballast on the AS-503 flight - . Nation: USA. Related Persons: Low, George. Program: Apollo. Flight: Apollo 8. Spacecraft: Apollo LTA, LM Weight.
George M. Low, ASPO Manager, set forth the rationale for using LTA-B (as opposed to some other LM test article or even a full-blown LM) as payload ballast on the AS-503 mission. That decision had been a joint one by Headquarters, MSFC, and MSC. Perhaps the chief reason for the decision was Marshall's position that the Saturn V's control system was extremely sensitive to payload weight. Numerous tests had been made for payloads of around 38,555 kilograms but none for those in the 29,435- to 31,750-kilogram range. MSFC had therefore asked that the minimum payload for AS-503 be set at 38,555 kilograms. Additional Details: here....

1968 September 10-11 - . Launch Vehicle: Saturn V.
The Apollo Crew Safety Review Board - . Nation: USA. Program: Apollo. Flight: Apollo 8. The Apollo Crew Safety Review Board, headed by William C. Schneider, met for the third time at MSFC, a meeting devoted primarily to safety factors for the Saturn V launch vehicle. . Additional Details: here....
1968 September 16 - . Launch Vehicle: Saturn V.
Changes in the Apollo Program Specification - . Nation: USA. Related Persons: Low, George. Program: Apollo.
Apollo Program Director Samuel C. Phillips formally notified ASPO Manager George M. Low at MSC and Saturn V Program Manager Lee B. James at MSFC of changes in the Apollo Program Specification. As agreed on during the MSF Management Council meeting on August 6, the Apollo payload interface was set at 46,040 kilograms (with a flight geometry reserve of 137 kilometers per hour). Also, the present spacecraft loading philosophy allowed a total spacecraft weight of 46,266 kilograms for lunar missions having less than maximum flight geometry requirements. Additional Details: here....

1968 October 1-2 - . Launch Vehicle: Saturn V.
The Apollo Crew Safety Review Board held its fourth meeting at MSC - . Nation: USA. Program: Apollo. Flight: Apollo 7. Spacecraft: Apollo CSM. The Apollo Crew Safety Review Board held its fourth meeting at MSC. . Additional Details: here....
1968 October 7 - . Launch Vehicle: Saturn V.
Apollo 8 CSM installed atop the Saturn V - . Nation: USA. Program: Apollo. Flight: Apollo 8. Spacecraft: Apollo CSM, CSM Block II.
In preparation for the flight of Apollo 8, NASA and industry technicians at KSC placed CSM 103 atop the Saturn V launch vehicle. The launch escape system was installed the following day; and on October 9 the complete AS-503 space vehicle was rolled out of the Vehicle Assembly Building and moved to the launch pad, where launch preparations were resumed.

1968 October 24 - . Launch Vehicle: Saturn V.
Retesting Saturn V following a lightning strike - . Nation: USA. Program: Apollo. Flight: Apollo 8. Howard D. Burns, Chief of the Saturn V Test Management Office at MSFC, sent to Apollo launch operations officials at KSC a list of requirements for retesting the Saturn V following a lightning strike on the vehicle while on the pad.. Additional Details: here....
1968 November 8 - . Launch Vehicle: Saturn V.
Proper spacecraft deployment during the Apollo 8 flight - . Nation: USA. Related Persons: Petrone. Program: Apollo. Flight: Apollo 7, Apollo 8. Spacecraft Bus: Apollo Spacecraft Systems Development Diaries. Spacecraft: CSM Electrical. ASPO Manager George M. Low asked Rocco A. Petrone, Launch Operations Director at KSC, to set up a special task team to review all paperwork and to inspect visually all hardware, to ensure proper spacecraft deployment during the Apollo 8 flight. . Additional Details: here....
1968 November 10 - . Launch Vehicle: Saturn V.
Success of Apollo 7 clears way for Apollo 8 lunar orbit mission in December. - . Nation: USA. Related Persons: Low, George. Program: Apollo. Flight: Apollo 7, Apollo 8. Spacecraft: Apollo CSM, Apollo LTA.
Apollo 7 - flown October 11-22 - far exceeded Low's expectations in results and left no doubts that they should go for lunar orbit on Apollo 8. At the November 10 Apollo Executive meeting Phillips presented a summary of the activities; James gave the launch vehicle status; Low reported on the spacecraft status and said he was impressed with the way KSC had handled its tight checkout schedule; Slayton reported on the flight plan; and Petrone on checkout readiness. Petrone said KSC could launch as early as December 10 or 12. Phillips said he would recommend to the Management Council the next day for Apollo 8 to go lunar orbit. Additional Details: here....

1968 November 11 - . Launch Vehicle: Saturn V.
Paine gives Apollo 8 go-ahead for lunar orbit mission. - . Nation: USA. Related Persons: Low, George, Paine. Program: Apollo. Flight: Apollo 8. Spacecraft: Apollo CSM, Apollo LTA. Low's initiative had paid off; the final decision to go to the moon in 1968 was made with the blessings of all of NASA's decision-makers, the Apollo Executive Committee, STAC, and PSAC..
1968 December 9 - . Launch Vehicle: Saturn V.
Launch preparations for Apollo 8 - . Nation: USA. Program: Apollo. Flight: Apollo 8. Spacecraft: Apollo CSM, CSM SPS. Launch preparations for Apollo 8, scheduled for flight December 21, were on schedule, the NASA Associate Administrator for Manned Space Flight reported. . Additional Details: here....
1968 December 21 - . 12:51 GMT - . Launch Site: Cape Canaveral. Launch Complex: Cape Canaveral LC39A. Launch Platform: LUT1. Launch Vehicle: Saturn V.
Apollo 8 - . Call Sign: Apollo 8. Crew: Anders, Borman, Lovell. Backup Crew: Aldrin, Armstrong, Haise. Payload: Apollo CSM 103 / LTA-B / S-IVB-503N. Mass: 28,833 kg (63,565 lb). Nation: USA. Related Persons: Aldrin, Anders, Armstrong, Borman, Haise, Lovell. Agency: NASA Houston. Program: Apollo. Class: Moon. Type: Manned lunar spacecraft. Flight: Apollo 8. Spacecraft: Apollo CSM. Duration: 6.13 days. Decay Date: 1968-12-27 . USAF Sat Cat: 3626 . COSPAR: 1968-118A. Apogee: 185 km (114 mi). Perigee: 185 km (114 mi). Inclination: 32.5000 deg. Period: 88.19 min.
Apollo 8 (AS-503) was launched from KSC Launch Complex 39, Pad A, at 7:51 a.m. EST Dec. 21 on a Saturn V booster. The spacecraft crew was made up of Frank Borman, James A. Lovell, Jr., and William A. Anders. Apollo 8 was the first spacecraft to be launched by a Saturn V with a crew on board, and that crew became the first men to fly around the moon.

All launch and boost phases were normal and the spacecraft with the S-IVB stage was inserted into an earth-parking orbit of 190.6 by 183.2 kilometers above the earth. After post-insertion checkout of spacecraft systems, the S-IVB stage was reignited and burned 5 minutes 9 seconds to place the spacecraft and stage in a trajectory toward the moon - and the Apollo 8 crew became the first men to leave the earth's gravitational field.

The spacecraft separated from the S-IVB 3 hours 20 minutes after launch and made two separation maneuvers using the SM's reaction control system. Eleven hours after liftoff, the first midcourse correction increased velocity by 26.4 kilometers per hour. The coast phase was devoted to navigation sightings, two television transmissions, and system checks. The second midcourse correction, about 61 hours into the flight, changed velocity by 1.5 kilometers per hour.

The 4-minute 15-second lunar-orbit-insertion maneuver was made 69 hours after launch, placing the spacecraft in an initial lunar orbit of 310.6 by 111.2 kilometers from the moon's surface - later circularized to 112.4 by 110.6 kilometers. During the lunar coast phase the crew made numerous landing-site and landmark sightings, took lunar photos, and prepared for the later maneuver to enter the trajectory back to the earth.

On the fourth day, Christmas Eve, communications were interrupted as Apollo 8 passed behind the moon, and the astronauts became the first men to see the moon's far side. Later that day , during the evening hours in the United States, the crew read the first 10 verses of Genesis on television to earth and wished viewers "goodnight, good luck, a Merry Christmas and God bless all of you - all of you on the good earth."

Subsequently, TV Guide for May 10-16, 1969, claimed that one out of every four persons on earth - nearly 1 billion people in 64 countries - heard the astronauts' reading and greeting, either on radio or on TV; and delayed broadcasts that same day reached 30 additional countries.

On Christmas Day, while the spacecraft was completing its 10th revolution of the moon, the service propulsion system engine was fired for three minutes 24 seconds, increasing the velocity by 3,875 km per hr and propelling Apollo 8 back toward the earth, after 20 hours 11 minutes in lunar orbit. More television was sent to earth on the way back.

1969 January 14 - . Launch Vehicle: Saturn V.
Arthur Rudolph, special assistant to the MSFC Director, retired - . Nation: USA. Related Persons: Rudolph. Program: Apollo.
MSFC announced that Arthur Rudolph, special assistant to the MSFC Director, would retire January 31. Rudolph had served as the manager of the Saturn V rocket program from August 1963 to May 1968. He was one of the more than 100 rocket experts who came to the United States from Germany in 1945. The MSC ASPO Manager, in a congratulatory letter said, "I will always consider Saturn V to be one of the outstanding achievements that occurred during my lifetime. Its sheer size is simply fantastic. But even more astounding was its performance in its first flights." Rudolph's work in bringing the nation's most powerful launch vehicle to flight status was rewarded when the first Saturn V lifted off from KSC and performed flawlessly on November 9, 1967, Rudolph's birthday.

1969 January 15-17 - . Launch Vehicle: Saturn V.
Final flight program for Apollo 9 verified - . Nation: USA. Program: Apollo. Flight: Apollo 9. Spacecraft: Apollo LM, LM Crew Station. The final flight program for Apollo 9 was verified; the emergency egress test with the prime and backup crew was conducted; and the software integration test between the lunar module and Mission Control Center, MSC, was completed on January 15. . Additional Details: here....
1969 March 3 - . 16:00 GMT - . Launch Site: Cape Canaveral. Launch Complex: Cape Canaveral LC39A. Launch Platform: LUT2. Launch Vehicle: Saturn V.
Apollo 9 - . Call Sign: Gumdrop. Crew: McDivitt, Schweickart, Scott. Backup Crew: Bean, Conrad, Gordon. Payload: Apollo CSM 104 / Apollo LM 3 / Saturn S-IVB-504N. Mass: 36,511 kg (80,492 lb). Nation: USA. Related Persons: Bean, Conrad, Gordon, McDivitt, Schweickart, Scott. Agency: NASA Houston. Program: Apollo. Class: Moon. Type: Manned lunar spacecraft. Flight: Apollo 9. Spacecraft: Apollo CSM. Duration: 10.04 days. Decay Date: 1969-03-13 . USAF Sat Cat: 3769 . COSPAR: 1969-018A. Apogee: 187 km (116 mi). Perigee: 185 km (114 mi). Inclination: 32.6000 deg. Period: 88.60 min.
Apollo 9 (AS-504), the first manned flight with the lunar module (LM-3), was launched from Pad A, Launch Complex 39, KSC, on a Saturn V launch vehicle at 11:00 a.m. EST March 3. Originally scheduled for a February 28 liftoff, the launch had been delayed to allow crew members James A. McDivitt, David R. Scott, and Russell L. Schweickart to recover from a mild virus respiratory illness. Following a normal launch phase, the S-IVB stage inserted the spacecraft into an orbit of 192.3 by 189.3 kilometers. After post-insertion checkout, CSM 104 separated from the S-IVB, was transposed, and docked with the LM. At 3:08 p.m. EST, the docked spacecraft were separated from the S-IVB, which was then placed on an earth-escape trajectory. On March 4 the crew tracked landmarks, conducted pitch and roll yaw maneuvers, and increased the apogee by service propulsion system burns.

On March 5 McDivitt and Schweickart entered the LM through the docking tunnel, evaluated the LM systems, transmitted the first of two series of telecasts, and fired the LM descent propulsion system. They then returned to the CM.

McDivitt and Schweickart reentered the LM on March 6. After transmitting a second telecast, Schweickart performed a 37-minute extravehicular activity (EVA), walking between the LM and CSM hatches, maneuvering on handrails, taking photographs, and describing rain squalls over KSC.

On March 7, with McDivitt and Schweickart once more in the LM, Scott separated the CSM from the LM and fired the reaction control system thrusters to obtain a distance of 5.5 kilometers between the two spacecraft. McDivitt and Schweickart then performed a lunar-module active rendezvous. The LM successfully docked with the CSM after being up to 183.5 kilometers away from it during the six-and-one-half-hour separation. After McDivitt and Schweickart returned to the CSM, the LM ascent stage was jettisoned.

During the remainder of the mission, the crew tracked Pegasus III, NASA's meteoroid detection satellite that had been launched July 30, 1965; took multispectral photos of the earth; exercised the spacecraft systems; and prepared for reentry.

Apollo 9 LM - . Call Sign: Spider. Payload: Apollo LM 3. Mass: 14,530 kg (32,030 lb). Nation: USA. Agency: NASA Houston. Program: Apollo. Class: Moon. Type: Manned lunar spacecraft. Flight: Apollo 9. Spacecraft: Apollo LM. Duration: 10.04 days. Decay Date: 1969-03-13 . USAF Sat Cat: 3769 . COSPAR: 1969-018x. Apogee: 187 km (116 mi). Perigee: 185 km (114 mi). Inclination: 32.6000 deg. Period: 88.60 min.
1969 March 11 - . Launch Vehicle: Saturn V.
Cost of the Apollo 204 fire $410 million - . Nation: USA. Related Persons: Mueller. Program: Apollo. Flight: Apollo 204. Spacecraft: Apollo LM.
The additional direct cost to the Apollo research and development program from the January 27, 1967, Apollo 204 fire was estimated at $410 million, principally for spacecraft modifications, NASA Associate Administrator for Manned Space Flight George E. Mueller testified in congressional hearings. The accident delayed the first manned flight of the spacecraft by about 18 months. "During this period, however, there occurred a successful unmanned test of the Lunar Module and two unmanned tests of the Saturn V vehicle."

1969 March 28 - . Launch Vehicle: Saturn V.
Apollo astronauts thrown forward during Saturn V S-IC/S-II stage separation - . Nation: USA. Program: Apollo. Flight: Apollo 9. Following a report by the Apollo 9 astronauts that they were thrown forward in their seats and had to grab their arm rests for support during the S-IC/S-II stage separation, an evaluation working group were studying the problem. . Additional Details: here....
1969 April 28 - . Launch Vehicle: Saturn V.
Apollo 10 launch vehicle damage - . Nation: USA. Program: Apollo. Flight: Apollo 10.
A power outage, required to permit maintenance work at the KSC Launch Control Center, was relayed to the pneumatic controls of the S-IC stage of the Apollo 10 launch vehicle, causing the prevalves to open and allowing 5,280 liters of RP-1 fuel to drain from the vehicle. Additional Details: here....

1969 May 2 - . Launch Vehicle: Saturn V.
Temporary fix for Apollo S-II-stage early center engine cutoff - . Nation: USA. Program: Apollo. Flight: Apollo 10, Apollo 12.
A temporary fix to provide for an S-II-stage early center engine cutoff was made for Apollo 10 and 11. Purpose was to eliminate oscillations of the center engine and sympathetic structures. Meanwhile, plans were being made to incorporate a permanent fix into Apollo 12 and subsequent vehicles to eliminate the oscillations.

1969 May 18 - . 16:49 GMT - . Launch Site: Cape Canaveral. Launch Complex: Cape Canaveral LC39B. Launch Platform: LUT3. Launch Vehicle: Saturn V.
Apollo 10 - . Call Sign: Charlie Brown. Crew: Cernan, Stafford, Young. Backup Crew: Cooper, Eisele, Mitchell. Payload: Apollo CSM 106 / Apollo LM 4 / Saturn S-IVB-505N. Mass: 28,870 kg (63,640 lb). Nation: USA. Related Persons: Cernan, Cooper, Eisele, Mitchell, Stafford, Young. Agency: NASA Houston. Program: Apollo. Class: Moon. Type: Manned lunar spacecraft. Flight: Apollo 10. Spacecraft: Apollo CSM. Duration: 8.00 days. Decay Date: 1969-05-26 . USAF Sat Cat: 3941 . COSPAR: 1969-043A. Apogee: 186 km (115 mi). Perigee: 185 km (114 mi). Inclination: 32.5000 deg. Period: 88.19 min.
Final dress rehearsal in lunar orbit for landing on moon. LM separated and descended to 10 km from surface of moon but did not land. Apollo 10 (AS-505) - with crew members Thomas P. Stafford, Eugene A. Cernan, and John W. Young aboard - lifted off from Pad B, Launch Complex 39, KSC, at 12:49 p.m. EDT on the first lunar orbital mission with complete spacecraft. The Saturn V's S-IVB stage and the spacecraft were inserted into an earth parking orbit of 189.9 by 184.4 kilometers while the onboard systems were checked. The S-IVB engine was then ignited at 3:19 p.m. EDT to place the spacecraft in a trajectory toward the moon. One-half hour later the CSM separated from the S-IVB, transposed, and docked with the lunar module. At 4:29 p.m. the docked spacecraft were ejected, a separation maneuver was performed, and the S-IVB was placed in a solar orbit by venting residual propellants. TV coverage of docking procedures was transmitted to the Goldstone, Calif., tracking station for worldwide, commercial viewing.

On May 19 the crew elected not to make the first of a series of midcourse maneuvers. A second preplanned midcourse correction that adjusted the trajectory to coincide with a July lunar landing trajectory was executed at 3:19 p.m. The maneuver was so accurate that preplanned third and fourth midcourse corrections were canceled. During the translunar coast, five color TV transmissions totaling 72 minutes were made of the spacecraft and the earth.

At 4:49 p.m. EDT on May 21 the spacecraft was inserted into a lunar orbit of 110.4 by 315.5 kilometers. After two revolutions of tracking and ground updates, a maneuver circularized the orbit at 109.1 by 113.9 kilometers. Astronaut Cernan then entered the LM, checked all systems, and returned to the CM for the scheduled sleep period.

On May 22 activation of the lunar module systems began at 11:49 a.m. EDT. At 2:04 p.m. the spacecraft were undocked and at 4:34 p.m. the LM was inserted into a descent orbit. One hour later the LM made a low-level pass at an altitude of 15.4 kilometers over the planned site for the first lunar landing. The test included a test of the landing radar, visual observation of lunar lighting, stereo photography of the moon, and execution of a phasing maneuver using the descent engine. The lunar module returned to dock successfully with the CSM following the eight-hour separation, and the LM crew returned to the CSM.

The LM ascent stage was jettisoned, its batteries were burned to depletion, and it was placed in a solar orbit on May 23. The crew then prepared for the return trip to earth and after 61.5 hours in lunar orbit a service propulsion system TEI burn injected the CSM into a trajectory toward the earth. During the return trip the astronauts made star-lunar landmark sightings, star-earth horizon navigation sightings, and live television transmissions.

Apollo 10 LM - . Call Sign: Snoopy. Payload: Apollo LM 4. Mass: 13,941 kg (30,734 lb). Nation: USA. Agency: NASA Houston. Program: Apollo. Class: Moon. Type: Manned lunar spacecraft. Flight: Apollo 10. Spacecraft: Apollo LM. Duration: 8.00 days. Decay Date: 1969-05-26 . USAF Sat Cat: 3941 . COSPAR: 1969-043x. Apogee: 186 km (115 mi). Perigee: 185 km (114 mi). Inclination: 32.5000 deg. Period: 88.19 min.
1969 June 3 - . Launch Vehicle: Saturn V.
Engineering evaluation of Apollo 10 launch vehicle - . Nation: USA. Program: Apollo. Flight: Apollo 10. The early engineering evaluation of the Apollo 10 launch vehicle, Saturn V AS-505, indicated that the major flight objectives were accomplished. . Additional Details: here....
1969 June 9-13 - . Launch Vehicle: Saturn V.
Studies of impact of empty Apollo stages on the lunar surface - . Nation: USA. Program: Apollo. Flight: Apollo 11, Apollo 12. Spacecraft: Apollo LM.
Studies were being conducted to determine the feasibility of intentionally impacting an S-IVB stage and an empty LM stage on the lunar surface after jettison, to gather geological data and enhance the scientific return of the seismology experiment. Data would be obtained with the ALSEP seismographic equipment placed on the lunar surface during the Apollo 11 or Apollo 12 flight. MSFC and Bellcomm were examining the possibility of the S-IVB jettison; MSC, the LM ascent stage jettison. Intentional impacting of the ascent stage for Apollo 11 was later determined not to be desirable.

1969 July 16 - . 13:32 GMT - . Launch Site: Cape Canaveral. Launch Complex: Cape Canaveral LC39A. Launch Platform: LUT1. Launch Vehicle: Saturn V.
Apollo 11 - . Call Sign: Columbia. Crew: Aldrin, Armstrong, Collins. Backup Crew: Anders, Haise, Lovell. Payload: Apollo CSM 107 / Apollo LM 5 / EASEP / S-IVB-506. Mass: 28,800 kg (63,400 lb). Nation: USA. Related Persons: Aldrin, Anders, Armstrong, Collins, Haise, Lovell. Agency: NASA Houston. Program: Apollo. Class: Moon. Type: Manned lunar spacecraft. Flight: Apollo 11. Spacecraft: Apollo CSM. Duration: 8.14 days. Decay Date: 1969-07-24 . USAF Sat Cat: 4039 . COSPAR: 1969-059A. Apogee: 186 km (115 mi). Perigee: 183 km (113 mi). Inclination: 32.5000 deg. Period: 88.19 min.
First landing on moon. Apollo 11 (AS-506) - with astronauts Neil A. Armstrong, Michael Collins, and Edwin E. Aldrin, Jr., aboard - was launched from Pad A, Launch Complex 39, KSC, at 9:32 a.m. EDT July 16. The activities during earth-orbit checkout, translunar injection, CSM transposition and docking, spacecraft ejection, and translunar coast were similar to those of Apollo 10.

At 4:40 p.m. EDT July 18, the crew began a 96-minute color television transmission of the CSM and LM interiors, CSM exterior, the earth, probe and drogue removal, spacecraft tunnel hatch opening, food preparation, and LM housekeeping. One scheduled and two unscheduled television broadcasts had been made previously by the Apollo 11 crew.

The spacecraft entered lunar orbit at 1:28 p.m. EDT on July 19. During the second lunar orbit a live color telecast of the lunar surface was made. A second service-propulsion-system burn placed the spacecraft in a circularized orbit, after which astronaut Aldrin entered the LM for two hours of housekeeping including a voice and telemetry test and an oxygen-purge-system check.

At 8:50 a.m. July 20, Armstrong and Aldrin reentered the LM and checked out all systems. They performed a maneuver at 1:11 p.m. to separate the LM from the CSM and began the descent to the moon. The LM touched down on the moon at 4:18 p.m. EDT July 20. Armstrong reported to mission control at MSC, "Houston, Tranquillity Base here - the Eagle has landed." (Eagle was the name given to the Apollo 11 LM; the CSM was named Columbia.) Man's first step on the moon was taken by Armstrong at 10:56 p.m. EDT. As he stepped onto the surface of the moon, Armstrong described the feat as "one small step for man - one giant leap for mankind."

Aldrin joined Armstrong on the surface of the moon at 11:15 p.m. July 20. The astronauts unveiled a plaque mounted on a strut of the LM and read to a worldwide TV audience, "Here men from the planet earth first set foot on the moon July 1969, A.D. We came in peace for all mankind." After raising the American flag and talking to President Nixon by radiotelephone, the two astronauts deployed the lunar surface experiments assigned to the mission and gathered 22 kilograms of samples of lunar soil and rocks. They then reentered the LM and closed the hatch at 1:11 a.m. July 21. All lunar extravehicular activities were televised in black-and-white. Meanwhile, Collins continued orbiting moon alone in CSM Columbia.

The Eagle lifted off from the moon at 1:54 p.m. EDT July 21, having spent 21 hours 36 minutes on the lunar surface. It docked with the CSM at 5:35 p.m. and the crew, with the lunar samples and film, transferred to the CSM. The LM ascent stage was jettisoned into lunar orbit. The crew then rested and prepared for the return trip to the earth.

The CSM was injected into a trajectory toward the earth at 12:55 a.m. EDT July 22. Following a midcourse correction at 4:01 p.m., an 18-minute color television transmission was made, in which the astronauts demonstrated the weightlessness of food and water and showed shots of the earth and the moon.

Apollo 11 LM - . Call Sign: Eagle. Payload: Apollo LM 5. Mass: 15,095 kg (33,278 lb). Nation: USA. Agency: NASA Houston. Program: Apollo. Class: Moon. Type: Manned lunar spacecraft. Flight: Apollo 11. Spacecraft: Apollo LM. Duration: 8.14 days. Decay Date: 1969-07-24 . USAF Sat Cat: 4039 . COSPAR: 1969-059x. Apogee: 186 km (115 mi). Perigee: 183 km (113 mi). Inclination: 32.5000 deg. Period: 88.19 min.
1969 August 1 - . Launch Vehicle: Saturn V.
Apollo 11 debriefing indicates a number of items requiring investigation - . Nation: USA. Program: Apollo. Flight: Apollo 11. Spacecraft: Apollo LM, CSM Hatch, LM Hatch. During the Apollo 11 management debriefing, the ASPO Manager noted a number of items requiring investigation. . Additional Details: here....
1969 November 14 - . 16:22 GMT - . Launch Site: Cape Canaveral. Launch Complex: Cape Canaveral LC39A. Launch Platform: LUT2. Launch Vehicle: Saturn V.
Apollo 12 - . Call Sign: Yankee Clipper. Crew: Bean, Conrad, Gordon. Backup Crew: Irwin, Scott, Worden. Payload: Apollo CSM 108 / Apollo LM 6 / ALSEP / S-IVB-507. Mass: 28,790 kg (63,470 lb). Nation: USA. Related Persons: Bean, Conrad, Gordon, Irwin, Scott, Worden. Agency: NASA Houston. Program: Apollo. Class: Moon. Type: Manned lunar spacecraft. Flight: Apollo 12. Spacecraft: Apollo CSM. Duration: 10.19 days. Decay Date: 1969-11-24 . USAF Sat Cat: 4225 . COSPAR: 1969-099A. Apogee: 186 km (115 mi). Perigee: 181 km (112 mi). Inclination: 32.5000 deg. Period: 88.19 min.
Apollo 12 (AS-507)-with astronauts Charles Conrad, Jr., Richard F. Gordon, Jr., and Alan L. Bean as the crewmen-was launched from Pad A, Launch Complex 39, KSC, at 11:22 a.m. EST November 14. Lightning struck the space vehicle twice, at 36.5 seconds and 52 seconds into the mission. The first strike was visible to spectators at the launch site. No damage was done. Except for special attention given to verifying all spacecraft systems because of the lightning strikes, the activities during earth-orbit checkout, translunar injection, and translunar coast were similar to those of Apollo 10 and Apollo 11.

During the translunar coast astronauts Conrad and Bean transferred to the LM one-half hour earlier than planned in order to obtain full TV coverage through the Goldstone tracking station. The 56-minute TV transmission showed excellent color pictures of the CSM, the intravehicular transfer, the LM interior, the earth, and the moon.

At 10:47 p.m. EST, November 17, the spacecraft entered a lunar orbit of 312.6 x 115.9 kilometers. A second service propulsion system burn circularized the orbit with a 122.5-kilometer apolune and a 100.6-kilometer perilune. Conrad and Bean again transferred to the LM, where they perfomed housekeeping chores, a voice and telemetry test, and an oxygen purge system check. They then returned to the CM.

Conrad and Bean reentered the LM, checked out all systems, and at 10:17 p.m. EST on November 18 fired the reaction control system thrusters to separate the CSM 108 (the Yankee Clipper) from the LM-6 (the Intrepid). At 1:55 a.m. EST November 19, the Intrepid landed on the moon's Ocean of Storms, about 163 meters from the Surveyor III spacecraft that had landed April 19, 1967. Conrad, shorter than Neil Armstrong (first man on the moon, July 20), had a little difficulty negotiating the last step from the LM ladder to the lunar surface. When he touched the surface at 6:44 a.m. EST November 19, he exclaimed, "Whoopee! Man, that may have been a small step for Neil, but that's a long one for me."

Bean joined Conrad on the surface at 7:14 a.m. They collected a 1.9-kilogram contingency sample of lunar material and later a 14.8-kilogram selected sample. They also deployed an S-band antenna, solar wind composition experiment, and the American flag. An Apollo Lunar Surface Experiments Package with a SNAP-27 atomic generator was deployed about 182 meters from the LM. After 3 hours 56 minutes on the lunar surface, the two astronauts entered the Intrepid to rest and check plans for the next EVA.

The astronauts again left the LM at 10:55 p.m. EST November 19. During the second EVA, Conrad and Bean retrieved the lunar module TV camera for return to earth for a failure analysis, obtained photographic panoramas, core and trench samples, a lunar environment sample, and assorted rock, dirt, bedrock, and molten samples. The crew then examined and retrieved parts of Surveyor III, including the TV camera and soil scoop. After 3 hours 49 minutes on the lunar surface during the second EVA, the two crewmen entered the LM at 2:44 a.m. EST November 20. Meanwhile astronaut Gordon, orbiting the moon in the Yankee Clipper, had completed a lunar multispectral photography experiment and photographed proposed future landing sites.

At 9:26 a.m. EST November 20, after 31 hours 31 minutes on the moon, Intrepid successfully lifted off with 34.4 kilograms of lunar samples. Rendezvous maneuvers went as planned. The LM docked with the CSM at 12:58 p.m. November 20. The last 24 minutes of the rendezvous sequence was televised. After the crew transferred with the samples, equipment, and film to the Yankee Clipper, the Intrepid was jettisoned and intentionally crashed onto the lunar surface at 5:17 p.m. November 20, 72.2 kilometers southeast of Surveyor III. The crash produced reverberations that lasted about 30 minutes and were detected by the seismometer left on the moon.

At 3:49 p.m. EST November 21, the crew fired the service propulsion system engine, injecting the CSM into a transearth trajectory after 89 hours 2 minutes in lunar orbit. During the transearth coast, views of the receding moon and the interior of the spacecraft were televised, and a question and answer session with scientists and the press was conducted.

Apollo 12 LM - . Call Sign: Intrepid. Payload: Apollo LM 6. Mass: 15,223 kg (33,560 lb). Nation: USA. Agency: NASA Houston. Program: Apollo. Class: Moon. Type: Manned lunar spacecraft. Flight: Apollo 12. Spacecraft: Apollo LM. Duration: 10.19 days. Decay Date: 1969-11-24 . USAF Sat Cat: 4225 . COSPAR: 1969-099x. Apogee: 186 km (115 mi). Perigee: 181 km (112 mi). Inclination: 32.5000 deg. Period: 88.19 min.
1970 January 4 - . Launch Vehicle: Saturn V.
NASA canceled the Apollo 20 mission and stretched out the remaining seven missions - . Nation: USA. Related Persons: Low, George. Program: Apollo. Flight: Apollo 20. Spacecraft: Apollo Lunar Landing.
NASA had canceled the Apollo 20 mission and stretched out the remaining seven missions to six-month intervals, Deputy Administrator George M. Low told the press in an interview after dedication of the Lunar Science Institute (next to MSC in Houston). Budget restrictions had brought the decision to suspend Saturn V launch vehicle production after vehicle 515 and to use the Apollo 20 Saturn V to launch the first U.S. space station in 1972.

1970 January 7 - . Launch Vehicle: Saturn V.
Saturn V launch vehicle 513 was designated for the first AAP Workshop launch. For planning purposes, launch vehicle 515 was being considered for use with either a backup or second Workshop. - . Nation: USA. Program: Skylab.
1970 April 11 - . 19:13 GMT - . Launch Site: Cape Canaveral. Launch Complex: Cape Canaveral LC39A. Launch Platform: LUT3. Launch Vehicle: Saturn V.
Apollo 13 - . Call Sign: Odyssey. Crew: Haise, Lovell, Swigert. Backup Crew: Duke, Mattingly, Young. Support Crew: Brand, Kerwin, Lousma. Payload: Apollo CSM 109 / Apollo LM 7 / ALSEP / S-IVB-508. Mass: 28,790 kg (63,470 lb). Nation: USA. Related Persons: Brand, Duke, Haise, Kerwin, Lousma, Lovell, Mattingly, Swigert, Young. Agency: NASA Houston. Program: Apollo. Class: Moon. Type: Manned lunar spacecraft. Flight: Apollo 13. Spacecraft: Apollo CSM. Duration: 5.95 days. Decay Date: 1970-04-17 . USAF Sat Cat: 4371 . COSPAR: 1970-029A. Apogee: 186 km (115 mi). Perigee: 184 km (114 mi). Inclination: 32.5000 deg. Period: 88.31 min.
Apollo 13 (AS-508) was launched from Pad A, Launch Complex 39, KSC, at 2:13 p.m. EST April 11, with astronauts James A. Lovell, Jr., John L. Swigert, Jr., and Fred W. Haise, Jr., aboard. The spacecraft and S-IVB stage entered a parking orbit with a 185.5-kilometer apogee and a 181.5-kilometer perigee. At 3:48 p.m., onboard TV was begun for five and one-half minutes. At 4:54 p.m., an S-IVB burn placed the spacecraft on a translunar trajectory, after which the CSM separated from the S-IVB and LM Aquarius. (The crew had named lunar module 7 Aquarius and CSM 109 Odyssey.) The CSM then hard-docked with the LM. The S-IVB auxiliary propulsion system made an evasive maneuver after CSM/LM ejection from the S-IVB at 6:14 p.m. The docking and ejection maneuvers were televised during a 72-minute period in which interior and exterior views of the spacecraft were also shown.

At 8:13 p.m. EST a 217-second S-IVB auxiliary propulsion system burn aimed the S-IVB for a lunar target point so accurately that another burn was not required. The S-IVB/IU impacted the lunar surface at 8:10 p.m. EST on April 14 at a speed of 259 meters per second. Impact was 137.1 kilometers from the Apollo 12 seismometer. The seismic signal generated by the impact lasted 3 hours 20 minutes and was so strong that a ground command was necessary to reduce seismometer gain and keep the recording on the scale. The suprathermal ion detector experiment, also deployed by the Apollo 12 crew, recorded a jump in the number of ions from zero at the time of impact up to 2,500 shortly thereafter and then back to a zero count. Scientists theorized that ionization had been produced by 6,300 K to 10,300 K (6,000 degrees C to 10,000 degrees C) temperature generated by the impact or that particles had reached an altitude of 60 kilometers from the lunar surface and had been ionized by sunlight.

Meanwhile back in the CSM/LM, the crew had been performing the routine housekeeping duties associated with the period of the translunar coast. At 30:40 ground elapsed time a midcourse correction maneuver took the spacecraft off a free-return trajectory in order to control the arrival time at the moon. Ensuring proper lighting conditions at the landing site. The maneuver placed the spacecraft on the desired trajectory, on which the closest approach to the moon would be 114.9 kilometers.

At 10:08 p.m. EST April 13, the crew reported an undervoltage alarm on the CSM main bus B, rapid loss of pressure in SM oxygen tank No. 2, and dropping current in fuel cells 1 and 3 to a zero reading. The loss of oxygen and primary power in the service module required an immediate abort of the mission. The astronauts powered up the LM, powered down the CSM, and used the LM systems for power and life support. The first maneuver following the abort decision was made with the descent propulsion system to place the spacecraft back in a free-return trajectory around the moon. After the spacecraft swung around the moon, another maneuver reduced the coast time back to earth and moved the landing point from the Indian Ocean to the South Pacific.

Apollo 13 LM - . Call Sign: Aquarius. Payload: Apollo LM 7. Mass: 15,192 kg (33,492 lb). Nation: USA. Agency: NASA Houston. Program: Apollo. Class: Moon. Type: Manned lunar spacecraft. Flight: Apollo 13. Spacecraft: Apollo LM. Duration: 5.95 days. Decay Date: 1970-04-17 . USAF Sat Cat: 4371 . COSPAR: 1970-029x. Apogee: 186 km (115 mi). Perigee: 184 km (114 mi). Inclination: 32.5000 deg. Period: 88.31 min.
1970 November 23 - . Launch Vehicle: Saturn V.
Saturn V launch vehicle SA-515 was designated as the backup launch vehicle for Skylab 1. Management responsibilities for the vehicle would be similar to those for the primary launch vehicle, SA-513. - . Nation: USA. Program: Skylab.
1971 January 31 - . 21:03 GMT - . Launch Site: Cape Canaveral. Launch Complex: Cape Canaveral LC39A. Launch Platform: LUT2. Launch Vehicle: Saturn V.
Apollo 14 - . Call Sign: Kitty Hawk. Crew: Mitchell, Roosa, Shepard. Backup Crew: Cernan, Engle, Evans. Support Crew: Chapman, McCandless, Pogue. Payload: Apollo CSM 110 / Apollo LM 8 / ALSEP / S-IVB-509. Mass: 29,230 kg (64,440 lb). Nation: USA. Related Persons: Cernan, Chapman, Engle, Evans, McCandless, Mitchell, Pogue, Roosa, Shepard. Agency: NASA Houston. Program: Apollo. Class: Moon. Type: Manned lunar spacecraft. Flight: Apollo 14. Spacecraft: Apollo CSM. Duration: 9.00 days. Decay Date: 1971-02-09 . USAF Sat Cat: 4900 . COSPAR: 1971-008A. Apogee: 183 km (113 mi). Perigee: 170 km (100 mi). Inclination: 31.1200 deg. Period: 88.18 min.
The Apollo 14 (AS-509) mission - manned by astronauts Alan B. Shepard, Jr., Stuart A. Roosa, and Edgar D. Mitchell - was launched from Pad A, Launch Complex 39, KSC, at 4:03 p.m. EST January 31 on a Saturn V launch vehicle. A 40-minute hold had been ordered 8 minutes before scheduled launch time because of unsatisfactory weather conditions, the first such delay in the Apollo program. Activities during earth orbit and translunar injection were similar to those of the previous lunar landing missions. However, during transposition and docking, CSM 110 Kitty Hawk had difficulty docking with LM-8 Antares. A hard dock was achieved on the sixth attempt at 9:00 p.m. EST, 1 hour 54 minutes later than planned. Other aspects of the translunar journey were normal and proceeded according to flight plan. A crew inspection of the probe and docking mechanism was televised during the coast toward the moon. The crew and ground personnel were unable to determine why the CSM and LM had failed to dock properly, but there was no indication that the systems would not work when used later in the flight.

Apollo 14 entered lunar orbit at 1:55 a.m. EST on February 4. At 2:41 a.m. the separated S-IVB stage and instrument unit struck the lunar surface 174 kilometers southeast of the planned impact point. The Apollo 12 seismometer, left on the moon in November 1969, registered the impact and continued to record vibrations for two hours.

After rechecking the systems in the LM, astronauts Shepard and Mitchell separated the LM from the CSM and descended to the lunar surface. The Antares landed on Fra Mauro at 4:17 a.m. EST February 5, 9 to 18 meters short of the planned landing point. The first EVA began at 9:53 a.m., after intermittent communications problems in the portable life support system had caused a 49-minute delay. The two astronauts collected a 19.5-kilogram contingency sample; deployed the TV, S-band antenna, American flag, and Solar Wind Composition experiment; photographed the LM, lunar surface, and experiments; deployed the Apollo lunar surface experiments package 152 meters west of the LM and the laser-ranging retroreflector 30 meters west of the ALSEP; and conducted an active seismic experiment, firing 13 thumper shots into the lunar surface.

A second EVA period began at 3:11 a.m. EST February 6. The two astronauts loaded the mobile equipment transporter (MET) - used for the first time - with photographic equipment, tools, and a lunar portable magnetometer. They made a geology traverse toward the rim of Cone Crater, collecting samples on the way. On their return, they adjusted the alignment of the ALSEP central station antenna in an effort to strengthen the signal received by the Manned Space Flight Network ground stations back on earth.

Just before reentering the LM, astronaut Shepard dropped a golf ball onto the lunar surface and on the third swing drove the ball 366 meters. The second EVA had lasted 4 hours 35 minutes, making a total EVA time for the mission of 9 hours 24 minutes. The Antares lifted off the moon with 43 kilograms of lunar samples at 1:48 p.m. EST February 6.

Meanwhile astronaut Roosa, orbiting the moon in the CSM, took astronomy and lunar photos, including photos of the proposed Descartes landing site for Apollo 16.

Ascent of the LM from the lunar surface, rendezvous, and docking with the CSM in orbit were performed as planned, with docking at 3:36 p.m. EST February 6. TV coverage of the rendezvous and docking maneuver was excellent. The two astronauts transferred from the LM to the CSM with samples, equipment, and film. The LM ascent stage was then jettisoned and intentionally crashed on the moon's surface at 7:46 p.m. The impact was recorded by the Apollo 12 and Apollo 14 ALSEPs.

The spacecraft was placed on its trajectory toward earth during the 34th lunar revolution. During transearth coast, four inflight technical demonstrations of equipment and processes in zero gravity were performed.

The CM and SM separated, the parachutes deployed, and other reentry events went as planned, and the Kitty Hawk splashed down in mid-Pacific at 4:05 p.m. EST February 9 about 7 kilometers from the recovery ship U.S.S. New Orleans. The Apollo 14 crew returned to Houston on February 12, where they remained in quarantine until February 26.

All primary mission objectives had been met. The mission had lasted 216 hours 40 minutes and was marked by the following achievements:

Third manned lunar landing mission and return.
Use of mobile equipment transporter (MET).
Payload of 32,500 kilograms placed in lunar orbit.
Distance of 3.3 kilometers traversed on lunar surface.
Payload of 43.5 kilograms returned from the lunar surface.
Lunar surface stay time of 33 hours.
Lunar surface EVA of 9 hours 47 minutes.
Use of shortened rendezvous technique.
Service propulsion system orbit insertion.
Active seismic experiment.
Inflight technical demonstrations.
Extensive orbital science period during CSM solo operations.
Apollo 14 LM - . Call Sign: Antares. Payload: Apollo LM 8. Mass: 15,279 kg (33,684 lb). Nation: USA. Agency: NASA Houston. Program: Apollo. Class: Moon. Type: Manned lunar spacecraft. Flight: Apollo 14. Spacecraft: Apollo LM. Duration: 9.00 days. Decay Date: 1971-02-09 . USAF Sat Cat: 4900 . COSPAR: 1971-008x. Apogee: 183 km (113 mi). Perigee: 170 km (100 mi). Inclination: 31.1200 deg. Period: 88.18 min.
1971 July 16 - . Launch Vehicle: Saturn V.
NASA approved the award to The Boeing Company of a contract modification for systems engineering and integration work on the Saturn V launch vehicle. - . Nation: USA. Program: Skylab.
The modification would extend Boeing's integration work through 31 December 1972. The basic contract began in September 1964. Included in the modification was work on requirements for Saturn V vehicles that would launch the remaining Apollo lunar exploration missions (Apollo 15, 16, and 17) and the Skylab Program's Saturn Workshop. Boeing's systems engineering and integration work at the time of this modification award included requirements and documentation for presettings for onboard computers that determined launch events, propellant loadings for all three vehicle stages, vehicle structural integrity, expected heating environments, range safety, tracking and communication data, and postflight reconstruction of launch data. Boeing was also MSFC's contractor for manufacture and testing of the first (S IC) stage of the Saturn V.

1971 July 26 - . 13:34 GMT - . Launch Site: Cape Canaveral. Launch Complex: Cape Canaveral LC39A. Launch Platform: LUT3. Launch Vehicle: Saturn V.
Apollo 15 - . Call Sign: Endeavour. Crew: Irwin, Scott, Worden. Backup Crew: Brand, Gordon, Schmitt. Payload: Apollo CSM 112/LM 10/ ALSEP/ LRV-1/PFS 1/S-IVB-510. Mass: 30,343 kg (66,894 lb). Nation: USA. Related Persons: Brand, Gordon, Irwin, Schmitt, Scott, Worden. Agency: NASA Houston. Program: Apollo. Class: Moon. Type: Manned lunar spacecraft. Flight: Apollo 15. Spacecraft: Apollo CSM. Duration: 12.30 days. Decay Date: 1971-08-07 . USAF Sat Cat: 5351 . COSPAR: 1971-063A. Apogee: 169 km (105 mi). Perigee: 166 km (103 mi). Inclination: 29.6800 deg. Period: 87.84 min.
Apollo 15 (AS-510) with astronauts David R. Scott, Alfred M. Worden, and James B. Irwin aboard was launched from Pad A, Launch Complex 39, KSC, at 9:34 a.m. EDT July 26. The spacecraft and S-IVB combination was placed in an earth parking orbit 11 minutes 44 seconds after liftoff. Activities during earth orbit and translunar injection (insertion into the trajectory for the moon) were similar to those of previous lunar landing missions. Translunar injection was at about 12:30 p.m., with separation of the CSM from the LM/S-IVB/IU at 12:56 p.m. At 1:08 p.m., onboard color TV showed the docking of the CSM with the LM.

S-IVB auxiliary propulsion system burns sent the S-IVB/IU stages toward the moon, where they impacted the lunar surface at 4:59 p.m. EDT July 29. The point of impact was 188 kilometers northeast of the Apollo 14 landing site and 355 kilometers northeast of the Apollo 12 site. The impact was detected by both the Apollo 12 and Apollo 14 seismometers, left on the moon in November 1969 and February 1971.

After the translunar coast, during which TV pictures of the CSM and LM interiors were shown and the LM communications and other systems were checked, Apollo 15 entered lunar orbit at 4:06 p.m. EDT July 29.

The LM-10 Falcon, with astronauts Scott and Irwin aboard, undocked and separated from the Endeavor (CSM 112) with astronaut Worden aboard. At 6:16 p.m. EDT July 30, the Falcon landed in the Hadley-Apennine region of the moon 600 meters north-northwest of the proposed target. About two hours later, following cabin depressurization, Scott performed a 33-minute standup EVA in the upper hatch of the LM, during which he described and photographed the landing site.

The first crew EVA on the lunar surface began at 9:04 a.m. July 31. The crew collected and stowed a contingency sample, unpacked the ALSEP and other experiments, and prepared the lunar roving vehicle (LRV) for operations. Some problems were encountered in the deployment and checkout of the LRV, used for the first time, but they were quickly resolved. The first EVA traverse was to the Apennine mountain front, after which the ALSEP was deployed and activated, and one probe of a Heat Flow experiment was emplaced. A second probe was not emplaced until EVA-2 because of drilling difficulties. The first EVA lasted 6 hours 33 minutes.

At 7:49 a.m. EDT August 1, the second EVA began. The astronauts made a maintenance check on the LRV and then began the second planned traverse of the mission. On completion of the traverse, Scott and Irwin completed the placement of heat flow experiment probes, collected a core sample, and deployed the American flag. They then stowed the sample container and the film in the LM, completing a second EVA of 7 hours 12 minutes.

The third EVA began at 4:52 a.m. August 2, included another traverse, and ended 4 hours 50 minutes later, for a total Apollo 15 lunar surface EVA time of 18 hours 35 minutes.

While the lunar module was on the moon, astronaut Worden completed 34 lunar orbits in the CSM operating scientific instrument module experiments and cameras to obtain data concerning the lunar surface and environment. X-ray spectrometer data indicated richer abundance of aluminum in the highlands, especially on the far side, but greater concentrations of magnesium in the maria.

Liftoff of the ascent stage of the LM, the first one to be televised, occurred at 1:11 p.m. EDT August 2. About two hours later the LM and CSM rendezvoused and docked, and film, equipment, and 77 kilograms of lunar samples were transferred from the LM to the CSM. The ascent stage was jettisoned and hit the lunar surface at 11:04 p.m. EDT August 2. Its impact was recorded by the Apollo 12, Apollo 14, and Apollo 15 seismometers, left on the moon during those missions. Before leaving the lunar orbit, the spacecraft deployed a subsatellite, at 4:13 p.m. August 4, in an orbit of 141.3 by 102 kilometers. The satellite would measure interplanetary and earth magnetic fields near the moon. It also carried charged-particle sensors and equipment to detect variations in lunar gravity caused by mascons (mass concentrations).

A transearth injection maneuver at 5:23 p.m. August 4 put the CSM on an earth trajectory. During the transearth coast, astronaut Worden performed an inflight EVA beginning at 11:32 a.m. August 5 and lasting for 38 minutes 12 seconds. He made three trips to the scientific instrument module (SIM) bay of the SM, twice to retrieve cassettes and once to observe the condition of the instruments in the SIM bay.

Apollo 15 LM - . Call Sign: Falcon. Payload: Apollo LM 10. Mass: 16,437 kg (36,237 lb). Nation: USA. Agency: NASA Houston. Program: Apollo. Class: Moon. Type: Manned lunar spacecraft. Flight: Apollo 15. Spacecraft: Apollo LM. Duration: 12.30 days. Decay Date: 1971-08-07 . USAF Sat Cat: 5351 . COSPAR: 1971-063x. Apogee: 169 km (105 mi). Perigee: 166 km (103 mi). Inclination: 29.6800 deg. Period: 87.84 min.
Apollo 15 Subsatellite - . Payload: PFS 1. Mass: 36 kg (79 lb). Nation: USA. Agency: NASA Houston. Program: Apollo. Class: Moon. Type: Lunar probe. Flight: Apollo 15. Spacecraft: PFS. USAF Sat Cat: 5377 . COSPAR: 1971-063D. Released from Apollo 15 into 102 x 142 km lunar orbit on 4 August 1971 at 20:13:29 GMT; studied lunar particles and included fields experiments. Last telemetry from lunar orbit in 1984..
1972 April 16 - . 17:54 GMT - . Launch Site: Cape Canaveral. Launch Complex: Cape Canaveral LC39A. Launch Platform: LUT3. Launch Vehicle: Saturn V.
Apollo 16 - . Call Sign: Caspar. Crew: Duke, Mattingly, Young. Backup Crew: Haise, Mitchell, Roosa. Payload: Apollo CSM 113/LM 11/ ALSEP/ LRV-2/PFS 2/S-IVB-511. Mass: 30,358 kg (66,927 lb). Nation: USA. Related Persons: Duke, Haise, Mattingly, Mitchell, Roosa, Young. Agency: NASA Houston. Program: Apollo. Class: Moon. Type: Manned lunar spacecraft. Flight: Apollo 16. Spacecraft: Apollo CSM. Duration: 11.08 days. Decay Date: 1972-04-27 . USAF Sat Cat: 6000 . COSPAR: 1972-031A. Apogee: 169 km (105 mi). Perigee: 167 km (103 mi). Inclination: 32.5420 deg. Period: 88.93 min.
The Apollo 16 (AS-511) space vehicle was launched from Pad A, Launch Complex 39, KSC, at 12:54 p.m. EST April 16, with a crew of astronauts John W. Young, Thomas K. Mattingly II, and Charles M. Duke, Jr. After insertion into an earth parking orbit for spacecraft system checks, the spacecraft and the S-IVB stage were placed on a trajectory to the moon at 3:28 p.m. CSM transposition and docking with the LM were achieved, although a number of minor anomalies were noted.

One anomaly, an auxiliary propulsion system leak on the S-IVB stage, produced an unpredictable thrust and prevented a final S-IVB targeting maneuver after separation from the CSM. Tracking of the S-IVB ended at 4:04 p.m. EST April 17, when the instrument unit's signal was lost. The stage hit the lunar surface at 4:02 p.m. April 19, 260 kilometers northeast of the target point. The impact was detected by the seismometers left on the moon by the Apollo 12, 14, and 15 missions.

Spacecraft operations were near normal during the coast to the moon. Unexplained light-colored particles from the LM were investigated and identified as shredded thermal paint. Other activities during the translunar coast included a cislunar navigation exercise, ultraviolet photography of the earth and moon, an electrophoresis demonstration, and an investigation of the visual light-flash phenomenon noted on previous flights. Astronaut Duke counted 70 white, instantaneous light flashes that left no after-glow.

Apollo 16 entered a lunar orbit of 314 by 107.7 kilometers at 3:22 p.m. April 19. After separation of LM-11 Orion from CSM 112 Casper, a CSM active rendezvous kept the two vehicles close together while an anomaly discovered on the service propulsion system was evaluated. Tests and analyses showed the redundant system to be still safe and usable if required. The vehicles were again separated and the mission continued on a revised timeline because of the 5 3/4-hour delay.

The lunar module landed with Duke and Young in the moon's Descartes region, about 230 meters northwest of the planned target area at 9:23 p.m. EST April 20. A sleep period was scheduled before EVA.

The first extravehicular activity began at 11:59 a.m. April 21, after the eight-hour rest period. Television coverage of surface activity was delayed until the lunar roving vehicle systems were activated, because the steerable antenna on the lunar module could not be used. The lunar surface experiments packages were deployed, but accidental breaking of the electronics cable rendered the heat flow experiment inoperable. After completing activities at the experiments site, the crew drove the lunar roving vehicle west to Flag Crater, where they performed the planned tasks. The inbound traverse route was just slightly south of the outbound route, and the next stop was Spook Crater. The crew then returned via the experiment station to the lunar module and deployed the solar wind composition experiment. The duration of the extravehicular activity was 7 hours 11 minutes. The distance traveled by the lunar roving vehicle was 4.2 kilometers. The crew collected 20 kilograms of samples.

The second extravehicular traverse, which began at 11:33 a.m. April 22, was south-southeast to a mare-sampling area near the Cinco Craters on Stone Mountain. The crew then drove in a northwesterly direction, making stops near Stubby and Wreck Craters. The last leg of the traverse was north to the experiments station and the lunar module. The second extravehicular activity lasted 7 hours 23 minutes. The distance traveled by the lunar roving vehicle was 11.1 kilometers.

Four stations were deleted from the third extravehicular traverse, which began 30 minutes early at 10:27 a.m. April 23 to allow extra time. The first stop was North Ray Crater, where "House Rock" on the rim of the crater was sampled. The crew then drove southeast to "Shadow Rock." The return route to the LM retraced the outbound route. The third extravehicular activity lasted 5 hours 40 minutes, and the lunar roving vehicle traveled 11.4 kilometers.

Lunar surface activities outside the LM totaled 20 hours 15 minutes for the mission. The total distance traveled in the lunar roving vehicle was 26.7 kilometers. The crew remained on the lunar surface 71 hours 14 minutes and collected 96.6 kilograms of lunar samples.

While the lunar module crew was on the surface, Mattingly, orbiting the moon in the CSM, was obtaining photographs, measuring physical properties of the moon and deep space, and making visual observations. Essentially the same complement of instruments was used to gather data as was used on the Apollo 15 mission, but different areas of the lunar surface were flown over and more comprehensive deep space measurements were made, providing scientific data that could be used to validate findings from Apollo 15 as well as add to the total store of knowledge of the moon and its atmosphere, the solar system, and galactic space.

The LM lifted off from the moon at 8:26 p.m. EST April 23, rendezvoused with the CSM, and docked with it in orbit. Young and Duke transferred to the CSM with samples, film, and equipment, and the LM was jettisoned the next day. LM attitude control was lost at jettison; therefore a deorbit maneuver was not possible and the LM remained in lunar orbit, with an estimated orbital lifetime of about one year.

The particles and fields subsatellite was launched into lunar orbit and normal system operation was noted. However, the spacecraft orbital shaping maneuver was not performed before ejection and the subsatellite was placed in a non-optimum orbit that resulted in a much shorter lifetime than the planned year. Loss of all subsatellite tracking and telemetry data on the 425th revolution (May 29) indicated that the subsatellite had hit the lunar surface.

The mass spectrometer deployment boom stalled during a retract cycle and was jettisoned before transearth injection. The second plane-change maneuver and some orbital science photography were deleted so that transearth injection could be performed about 24 hours earlier than originally planned.

Activities during the transearth coast phase of the mission included photography for a contamination study for the Skylab program and completion of the visual light-flash-phenomenon investigation that had been partially accomplished during translunar coast. A 1-hour 24-minute transearth extravehicular activity was conducted by command module pilot Mattingly to retrieve the film cassettes from the scientific instrument module cameras, inspect the equipment, and expose a microbial-response experiment to the space environment. Two midcourse corrections were made on the return flight to achieve the desired entry interface conditions.

Apollo 16 LM - . Call Sign: Orion. Payload: Apollo LM 11. Mass: 16,437 kg (36,237 lb). Nation: USA. Agency: NASA Houston. Program: Apollo. Class: Moon. Type: Manned lunar spacecraft. Flight: Apollo 16. Spacecraft: Apollo LM. Duration: 11.08 days. Decay Date: 1972-04-27 . USAF Sat Cat: 6000 . COSPAR: 1972-031x. Apogee: 169 km (105 mi). Perigee: 167 km (103 mi). Inclination: 32.5420 deg. Period: 88.93 min.
Apollo 16 Subsatellite - . Payload: PFS 2. Mass: 36 kg (79 lb). Nation: USA. Agency: NASA Houston. Program: Apollo. Class: Moon. Type: Lunar probe. Flight: Apollo 16. Spacecraft: PFS. Decay Date: 1972-05-29 . USAF Sat Cat: 6009 . COSPAR: 1972-031D. Released from Apollo 16 into lunar orbit on 24 April 1972 at 21:56:09 GMT into a 96 km x 122 km orbit; fields and particles data; impacted lunar surface 29 May 1972..
1972 December 7 - . 05:33 GMT - . Launch Site: Cape Canaveral. Launch Complex: Cape Canaveral LC39A. Launch Platform: LUT3. Launch Vehicle: Saturn V.
Apollo 17 - . Call Sign: America. Crew: Cernan, Evans, Schmitt. Backup Crew: Duke, Roosa, Young. Payload: Apollo CSM 114/LM 12/ ALSEP/ LRV-3/S-IVB-512. Mass: 30,342 kg (66,892 lb). Nation: USA. Related Persons: Cernan, Duke, Evans, Roosa, Schmitt, Young. Agency: NASA Houston. Program: Apollo. Class: Moon. Type: Manned lunar spacecraft. Flight: Apollo 17. Spacecraft: Apollo CSM. Duration: 12.58 days. Decay Date: 1972-12-19 . USAF Sat Cat: 6300 . COSPAR: 1972-096A. Apogee: 167 km (103 mi). Perigee: 167 km (103 mi). Inclination: 28.5260 deg. Period: 87.83 min.
Apollo 17 (AS-512), the final Apollo manned lunar landing mission, was launched from Pad A, Launch Complex 39, KSC, at 12:33 a.m. EST December 7. Crew members were astronauts Eugene A. Cernan, Ronald E. Evans, and Harrison H. Schmitt. The launch had been delayed 2 hours 40 minutes by a countdown sequencer failure, the only such delay in the Apollo program caused by a hardware failure.

All launch vehicle systems performed normally in achieving an earth parking orbit of 170 by 168 kilometers. After checkout, insertion into a lunar trajectory was begun at 3:46 a.m.; translunar coast time was shortened to compensate for the launch delay. CSM 114 transposition, docking with LM-12, and LM ejection from the launch vehicle stage were normal. The S-IVB stage was maneuvered for lunar impact, striking the surface about 13.5 kilometers from the preplanned point at 3:27 p.m. EST December 10. The impact was recorded by the passive seismometers left on the moon by Apollo 12, 14, 15, and 16.

The crew performed a heat flow and convection demonstration and an Apollo light-flash experiment during the translunar coast. The scientific instrument module door on the SM was jettisoned at 10:17 a.m. EST December 10. The lunar orbit insertion maneuver was begun at 2:47 p.m. and the Apollo 17 spacecraft entered a lunar orbit of 315 by 97 kilometers. After separation of the LM Challenger from the CSM America and a readjustment of orbits, the LM began its powered descent and landed on the lunar surface in the Taurus-Littrow region at 2:55 p.m. EST on December 11, with Cernan and Schmitt.

The first EVA began about 4 hours later (6:55 p.m.). Offloading of the lunar roving vehicle and equipment proceeded as scheduled. The Apollo Lunar Surface Experiment Package was deployed approximately 185 meters west northwest of the Challenger. Astronaut Cernan drove the lunar roving vehicle to the experiments deployment site, drilled the heat flow and deep core holes, and emplaced the neutron probe experiment. Two geological units were sampled, two explosive packages deployed, and seven traverse gravimeter measurements were taken. During the 7-hour 12-minute EVA, 14 kilograms of samples were collected.

The second extravehicular activity began at 6:28 p.m. EST December 12. Because of geological interest, station stop times were modified. Orange soil was discovered and became the subject of considerable geological discussion. Five surface samples and a double core sample were taken in the area of the orange soil. Three explosive packages were deployed, seven traverse gravimeter measurements were taken, and observations were photographed. Samples collected totaled 34 kilograms during the 7 hours and 37 minutes of the second EVA.

The third and final EVA began at 5:26 p.m. EST December 13. Specific sampling objectives were accomplished. Samples - including blue-gray breccias, fine-grained vesicular basalts, crushed anorthositic rocks, and soils - weighed 66 kilograms. Nine traverse gravimeter measurements were made. The surface electrical properties experiment was terminated. Before reentering the LM, the crew selected a breccia rock to dedicate to the nations represented by students visiting the Mission Control Center. A plaque on the landing gear of the lunar module, commemorating all of the Apollo lunar landings, was then unveiled. After 7 hours 15 minutes, the last Apollo EVA on the lunar surface ended. Total time of the three EVAs was approximately 22 hours; the lunar roving vehicle was driven 35 kilometers, and about 115 kilograms of lunar sample material was acquired.

While Cernan and Schmitt were exploring the lunar surface, Evans was conducting numerous scientific activities in the CSM in lunar orbit. In addition to the panoramic camera, the mapping camera, and the laser altimeter, three new scientific instrument module experiments were included in the Apollo 17 orbital science equipment. An ultraviolet spectrometer measured lunar atmospheric density and composition; an infrared radiometer mapped the thermal characteristics of the moon; and a lunar sounder acquired data on the subsurface structure.

Challenger lifted off the moon at 5:55 p.m. EST December 14. Rendezvous with the orbiting CSM and docking were normal. The two astronauts transferred to the CM with samples and equipment and the LM ascent stage was jettisoned at 1:31 a.m. December 15. Its impact on the lunar surface about 1.6 kilometers from the planned target was recorded by four Apollo 17 geophones and the Apollo 12, 14, 15, and 16 seismometers emplaced on the surface. The seismic experiment explosive packages that had been deployed on the moon were detonated as planned and recorded on the geophones.

During the coast back to earth, Evans left the CSM at 3:27 p.m. EST December 17 for a 1-hour 7-minute inflight EVA and retrieved lunar sounder film and panoramic and mapping camera cassettes from the scientific instrument module bay. The crew conducted the Apollo light- flash experiment and operated the infrared radiometer and ultraviolet spectrometer.

Reentry, landing, and recovery were normal. The command module parachuted into the mid-Pacific at 2:25 p.m. EST December 19, 6.4 kilometers from the prime recovery ship, U.S.S. Ticonderoga. The crew was picked up by helicopter and was on board the U.S.S. Ticonderoga 52 minutes after the CM landed. All primary mission objectives had been achieved.

Apollo 17 LM - . Call Sign: Challenger. Payload: Apollo LM 12. Mass: 16,448 kg (36,261 lb). Nation: USA. Agency: NASA Houston. Program: Apollo. Class: Moon. Type: Manned lunar spacecraft. Flight: Apollo 17. Spacecraft: Apollo LM. Duration: 12.58 days. Decay Date: 1972-12-19 . USAF Sat Cat: 6300 . COSPAR: 1972-096x. Apogee: 167 km (103 mi). Perigee: 167 km (103 mi). Inclination: 28.5260 deg. Period: 87.83 min.
1973 January 19 - . Launch Vehicle: Saturn V.
Plan for storage of unassigned Saturn hardware and phaseout of Saturn V. - . Nation: USA. Program: Skylab.
MSFC began implementation of a plan for preparation and storage of unassigned Saturn hardware, phaseout of the Saturn V production capability, and amendment of the facility operations contract at the Michoud Assembly Facility for minimum surveillance of stored hardware.

1973 May 14 - . 17:30 GMT - . Launch Site: Cape Canaveral. Launch Complex: Cape Canaveral LC39A. Launch Platform: LUT2. Launch Vehicle: Saturn V.
Skylab 1 - . Payload: Skylab Orbital Workshop. Mass: 74,783 kg (164,868 lb). Nation: USA. Agency: NASA Huntsville. Program: Skylab. Class: Manned. Type: Manned space station. Spacecraft: Skylab. Decay Date: 1979-07-11 . USAF Sat Cat: 6633 . COSPAR: 1973-027A. Apogee: 439 km (272 mi). Perigee: 427 km (265 mi). Inclination: 50.0000 deg. Period: 93.20 min.
First and only US space station to date. Project began life as Apollo Orbital Workshop - outfitting of an S-IVB stage with docking adapter with equipment launched by several subsequent S-1B launches. Curtailment of the Apollo moon landings meant that surplus Saturn V's were available, so the pre-equipped, five times heavier, and much more capable Skylab resulted.

An unexpected telemetry indication of meteoroid shield deployment and solar array wing 2 beam fairing separation was received 1 minute and 3 seconds after liftoff. However, all other systems of the OWS appeared normal, and the OWS was inserted into a near-circular Earth orbit of approximately 435 km altitude. The payload shroud was jettisoned, and the ATM with its solar array was deployed as planned during the first orbit. Deployment of the Workshop solar array and the meteoroid shield was not successful. In fact the xternal solar/meteoroid shield had ripped off 63 seconds into ascent, tearing away one solar panel wing and debris jamming the remaining panel. Without shield temperatures soared in station. Repairs by crews led to virtually all mission objectives being met.

Following the final manned phase of the Skylab mission, ground controllers performed some engineering tests of certain Skylab systems--tests that ground personnel were reluctant to do while men were aboard. Results from these tests helped to determine causes of failures during the mission and to obtain data on long term degradation of space systems.

Upon completion of the engineering tests, Skylab was positioned into a stable attitude and systems were shut down. It was expected that Skylab would remain in orbit eight to ten years. It was to have been visited by an early shuttle mission, reboosted into a higher orbit, and used by space shuttle crews. But delays in the first flight of the shuttle made this impossible.

On July 11, 1979, Skylab disintegrated when it re-entered the earth's atmosphere after a worldwide scare over its pending crash. The debris stretched from the south-east Indian Ocean into Western Australia. Additional Details: here....

Home - Search - Browse - Alphabetic Index: 0- 1- 2- 3- 4- 5- 6- 7- 8- 9
A- B- C- D- E- F- G- H- I- J- K- L- M- N- O- P- Q- R- S- T- U- V- W- X- Y- Z
© 1997-2017 Mark Wade - Contact 
© / Conditions for Use

"""

# Parse the document with spaCy
doc = nlp(text)

# Extract semi-structured statements
statements = textacy.extract.semistructured_statements(doc, "Saturn V")

acronyms = textacy.extract.acronyms_and_definitions(doc)

quotations = textacy.extract.direct_quotations(doc)

namedEntities = textacy.extract.named_entities(doc)

keyTerms = textacy.keyterms.key_terms_from_semantic_network(doc)

# Print the results
print("Here are the things I know about Saturn V:")

for statement in statements:
    subject, verb, fact = statement
    print(' - {}'.format(fact))

print("Here are the acronyms and definitions I found about Saturn V:")

for acronym in acronyms:
    if acronyms[acronym] is not '':
      print(' - {}: {}'.format(acronym, acronyms[acronym]))

print("Here are the direct quoations I found about Saturn V:")

for quote in quotations:
    speaker, verb, quotation = quote
    print(' - {}: {}'.format(speaker, quotation))

# print("Here are the named entities I found about # Saturn V:")
# 
# for entity in namedEntities:
#     print(' - {}'.format(entity))

print("Here are the terms I found for Saturn V:")

for keyTerm in keyTerms:
    term, ranking = keyTerm
    print(' - {} rank: {}'.format(term, ranking))