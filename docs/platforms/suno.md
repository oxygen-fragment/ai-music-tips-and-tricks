# Techniques that have been tested with Suno

## Simple vs. Custom tab

In Suno, switching between the Simple and Custom tabs has a number of effects.

![suno-simple-custom-tabs.PNG](/images/suno-simple-custom-tabs.PNG)

From my testing, I've noticed the following effects:

### Simple

Suno will infer a lot more using your prompt.

**Example:** "Complex melodic runs (30 seconds maximum)" turns into, "piano-driven, with complex melodic runs and dynamic builds, intricate, pop, complex".

**NOTE:** During testing, Suno did **not** adhere to the parenthesized instructions, i.e. Suno created a 2 minute 30 second plus song.

### Custom

Suno is faithful to whatever prompt you use.

**Example:** "Complex melodic runs (30 seconds maximum)" stays exactly the same.

**NOTE:** Songs generated were under 30 seconds in length.

## Song Length

By default, Suno seems to generate songs that are around 2 minutes 30 seconds in length for instrumental tracks. You can adjust this using parentheses `()`.

**Example:**

`Simple melodic line (30 seconds maximum)`

During testing, I found that it generated two versions, one 18 seconds and the other 29 seconds.

## Song Structure and Lyrics

### Chorus

```
[chorus]
Repeat
```

With the chorus, you only need to define the lyrics *once*. After the first chorus, you can use the above instead of repeating the entire chorus each time.

### Lyrics

Leave lyrics blank for an instrumental track.
