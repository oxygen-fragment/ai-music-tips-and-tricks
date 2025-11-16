# Techniques that have been tested with Suno

## Simple vs. Custom tab

In Suno, switching between the Simple and Custom tabs has a number of effects.

![suno-simple-custom-tabs.PNG](/images/suno-simple-custom-tabs.PNG)

From my testing, I've noticed the following effects:

### Simple

Suno will infer a lot more using your prompt.

**Example:**

>Complex melodic runs (30 seconds maximum)

turns into,

>piano-driven, with complex melodic runs and dynamic builds, intricate, pop, complex

**NOTE:** During testing, Suno did **not** adhere to the parenthesized instructions, i.e. Suno created a 2 minute 30 second plus song.

### Custom

Suno is faithful to whatever prompt you use.

**Example:**

>Complex melodic runs (30 seconds maximum)

Stays exactly the same.

**NOTE:** Songs generated were under 30 seconds in length.

## Song Length

By default, Suno seems to generate songs that are around 2 minutes 30 seconds in length for instrumental tracks. You can adjust this using parentheses `()`.

**Example:**

`Simple melodic line (30 seconds maximum)`

During testing, I found that it generated two versions, one 18 seconds and the other 29 seconds.

## Add Audio

Upload audio and Suno will generate a detailed description that can be used as a prompt.

## Add Persona

Reuse a persona you've saved.

## Add Inspo (Inspiration)

When you want to take inspiration from your previously created songs (select from your playlists).

## Advanced Options

### Exclude styles

{ADD STUFF HERE}

### Voice Gender

Male/Female

{ADD STUFF HERE}

### Lyrics Mode

Manual/Auto

{ADD STUFF HERE}

### Weirdness

0-100%

#### Observed Weirdness Effects

{STUFF HERE}

### Style Influence

0-100%

85%+ "danger zone"

#### Observed Style Influence Effects

- `> 85%`: increased chance of unwanted audio artifacts (think: scratched CD)

## Song Structure and Lyrics

### Chorus

```
[chorus]
Repeat
```

With the chorus, you only need to define the lyrics *once*. After the first chorus, you can use the above instead of repeating the entire chorus each time.

### Lyrics

Leave lyrics blank for an instrumental track.

## Quirks

### Multiple Selections

When selecting multiple tracks, it's not clear what you can do. To take some action on all you've selected, after selection, click on the 3 dots on any of the selected songs and pick from that menu.

### Parentheses (extra instructions)

Through testing it was discovered that Suno will adhere to **one** instruction that is provided in parentheses. For example:

>[first part of your prompt] (30 seconds maximum)

Will yield a 30 second or less song.

Having two instructions in parentheses seems to confuse the model. Example:

>Slow tempo (60 BPM, 30 seconds maximum)

Suno provided a 31 second and a 59 second song.  This may have been due to "60 BPM" being redundant, will require more testing.

### UI

- Pressing `Enter` in the Publish song screen doesn't publish
