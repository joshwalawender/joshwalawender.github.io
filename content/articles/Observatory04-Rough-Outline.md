Title: Backyard Observatory Build 4 - A Rough Outline
Date: 2021-03-22
Author: Josh Walawender
Header_Cover: images/IMG_5030.jpg
Category: Observatory Build
Tags: Astronomy, Observatory Design
Slug: observatory04-rough-outline
Status: draft

As I've been thinking about the design of this observatory a few choices about design had to be made.

## Dome or Roll Off Roof?

As I mentioned in my earlier discussion of the [weather](observatory02-weather) here, I expect wind will be a major impact on the observatory.  Wind shake will be a factor for a telescope unless the observatory can provide significant protection.  For this reason, I'd initially thought about using a dome style observatory.  I'm not really a big fan of domes for small observatories.  It seems like many people build them for the look, but I wanted something a bit more subtle.  I also prefer the simplicity of a roll off roof.  The control system and electronics are far simpler because there's no need to bridge electricity across to the rotating part of the dome in order to operate the shutter.  While this is not too difficult these days (during my time as a postdoc I built a pair of robotic domed observatories), I wanted to keep my own build as simple as possible.  As a result, I decided that I was willing to live with the lesser wind protection of a roll off roof and perhaps sacrifice horizon access for wind protection by having relatively tall walls.

Even though this is a roll off roof, I'll keep the walls relatively high to shield the telescope.  Balancing this will be tough because I also want to keep the overall building small which brings the walls in close to the telescope, but that further increases their impact on the horizon (though it also provides more wind protection).

Keeping the walls high provides another advantage: the telescope should be able to slew around inside the closed observatory.  This is important because if the roof can not hit the telescope at any position, then it will be able to close without waiting for the telescope to park.  This is really nice because if there is a problem with the telescope mount, you may not be able to close the roof in case of bad weather.  That entire class of problem goes away if you can open and close the roof without worrying about the telescope position.

In addition, one can connect the weather station to the roof controller directly and have the weather station trigger a close without going through the control software.  This eliminates another entire class of failure:  if the computer software has crashed the computer, the system will still close in the event of bad weather.  In my experience with robotic observatories as a postdoc, I encountered first hand how important this can be and how much easier it will be for me to sleep while the system is in operation.

## Concrete Slab or Deck Flooring?

This question was always a relatively easy one for me.  Concrete is a thermal mass which would radiate heat away during the night and cause seeing issues.  The big research telescopes are built on concrete foundations, but they are also air conditioned during the day so that the interior (including the concrete flooring) is kept at nighttime temperatures.

To be fair, I doubt this would have a big negative effect on a small observatory like the one I have in mind.  In addition, while being on the ["dry side" of Waimea](observatory02-weather) means I have some clear skies, it also means that I'm on the lee side of a mountain range, so I don't expect great seeing on typical night.  Just going out and watching the twinkling of stars by eye, I can tell there are a number of nights with truly poor seeing that I'll be dealing with.

I also didn't want to deal with arranging for a cement truck and pouring a large cement pad.  It will likely be more work to build footings and a deck, but I prefer that solution.

## What Dimensions?

How big should this observatory be?  One of my initial ideas was to build a really small observatory (maybe 4 feet square) geared toward housing a single short focus refractor on a compact mount.  The original idea was to be as small as possible to the point where a human wouldn't be able to go inside comfortably.  To work on the equipment, one would open the roof and lean in over the walls.

I moved away from this idea since the dimensions would be tightly coupled to exactly which mount and telescope were in use.  If I changed equipment in the future, it might not fit in the observatory.

I also worried that most of the cost and challenges would not be substantially reduced by pushing the size down beyond a certain point.  My intention is to design this with the idea that it will be fully robotic at some point, so roof mechanisms need to be motorized and there are little or no cost savings or simplifications on that front by going really small.

## What To Do With the Area Under the Gantry?

In browsing books and web sites about amateur observatories, one sees that people usually do one of two things with the area under the gantry where the roof rolls off.  Most either leave the space open (perhaps incorporating a seating area) or enclose it as a "warm room" where an observer can sit and control the telescope.  For me, the warm room option was not appealing.  As I mentioned before, I plan to make this remote or robotic, so I can sit in my office in the main house to control things.  A deck or seating area was an option, but in the end I've decided to enclose the area under the gantry as storage.  

Like many amateur astronomers I have quiet a few astro toys taking up space in the garage.  If I can move them out to a dedicated storage area that frees up more workspace in the garage.  Living in Hawaii, I have to worry about the conditions where I store my astro gear.  In the humid conditions of the tropics, mold can grow on just about anything, including optics.  I've seen a number of telescope mirrors or camera lenses with mold growing on the coatings and which, if left alone, will actually etch the glass.  As a result, I keep all my gear in boxes with desiccant packs to try to redce the humidity.  For larget items, I keep them in a room with a dehumidifier.  At the moment, this is my garage which is a pretty large volume for the dehumidifier to try to dry out.  I'm hoping that I can move the dehumidifier to the observatory and have it keep the storage area nice and dry with the side benefit of keeping the air in the observatory dry during times when the roof is closed.

I'm not sure this dry storage area will work out as planned, but this is the goal for now.  If it doesn't work out, I'll end up with the under-gantry section as a true garden shed for storing a lawnmower or other garden tools.