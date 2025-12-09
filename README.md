# Song Class Overview

The `Song` class models basic song data while maintaining shared, class-level information about all songs that have been created. Each instance stores its own name, artist, and genre, while the class tracks global statistics across every `Song` object.

## Features

### Instance Attributes
Each `Song` stores:
- **name** – The title of the song.
- **artist** – The performing artist.
- **genre** – The musical genre of the song.

These values are set when a new `Song` object is created.

### Class-Level Tracking
The class keeps cumulative data shared across all instances:

- **`Song.count`**  
  Total number of `Song` objects created.

- **`Song.genres`**  
  A list of all genres from every instantiated song.

- **`Song.artists`**  
  A list of all artists from every instantiated song.

- **`Song.genre_count`**  
  A dictionary mapping each genre to the number of songs in that genre.

- **`Song.artist_count`**  
  A dictionary mapping each artist to the number of songs created for that artist.

### Automatic Bookkeeping
Whenever a new `Song` is initialized, the class automatically:
- Increments the global song counter  
- Records the song's genre and artist  
- Updates the total count for that genre  
- Updates the total count for that artist  

All bookkeeping is handled internally using class methods, so users only need to create `Song` objects for the tracking system to update.

---

