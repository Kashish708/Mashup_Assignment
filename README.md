

# Mashup Generator – Assignment Submission

## Assignment Description

The system:

- Downloads N YouTube videos of a given singer
- Converts videos to audio (MP3)
- Extracts the first Y seconds from each audio
- Merges all trimmed audio clips into one mashup file
- Provides both Command Line and Web-based implementation

---

## Program 1 – Command Line Mashup Generator

##  File Name Format

```
<RollNumber>.py
Example: 102317186.py
```

---

##  How to Run

```
python <program.py> <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>
```

### Example:

```
python 102317186.py "Sharry Maan" 20 25 mashup.mp3
```

---

##  Required Libraries

Install the required packages:

```
pip install yt-dlp pydub
```

Also, install **FFmpeg** and add it to the system PATH.

---

# Methodology

The program follows these major steps:

---

##  Input Validation

The program checks:

- Correct number of command line arguments
- NumberOfVideos must be greater than 10
- AudioDuration must be greater than 20 seconds
- Integer validation for numeric inputs
- Proper exception handling for errors

If any validation fails, appropriate error messages are displayed, and the program exits safely.

---

##  Video Downloading

- Uses `yt_dlp` library
- Searches YouTube using:

```
ytsearch<N>:<SingerName> songs
```

- Downloads the best available audio format
- Converts automatically to MP3
- Stores files inside `downloads/` folder

---

##  Audio Trimming

- Each MP3 file is loaded using `pydub`
- First Y seconds extracted
- Duration conversion:

```
Milliseconds = Y × 1000
```

- Trimmed clips stored in memory

---

## Audio Merging

- All trimmed audio clips are concatenated
- Final mashup exported as:

```
<OutputFileName>.mp3
```

---

## Result Analysis

##  Sample Test Case

| Parameter        | Value       |
|------------------|-------------|
| Singer Name      | Sharry Maan |
| Number of Videos | 20          |
| Duration (sec)   | 25          |
| Output File      | mashup.mp3  |

---

##  Result Table

| Step                  | Result     |
|-----------------------|------------|
| Videos Downloaded     | 20         |
| Duration per Clip     | 25 sec     |
| Total Clips Merged    | 20         |
| Final Mashup Duration | ~500 sec   |
| Output Generated      | mashup.mp3 |

---

##  Result Graph Explanation

Let:

- N = Number of Videos
- Y = Duration per Video (seconds)

Then:

```
Final Mashup Duration = N × Y
```

Example:

```
20 × 25 = 500 seconds
```

This shows a **linear relationship** between the number of videos and the final mashup duration.

As the number of videos increases, the final mashup duration increases proportionally.

---

## Program 2 – Web Service Implementation

##  Features

User provides:

- Singer Name
- Number of Videos
- Duration
- Email ID

System:

- Validates inputs
- Generates a mashup
- Creates ZIP file
- Sends a ZIP file via email

---

##  Technologies Used

- Python
- Flask (Web Framework)
- yt_dlp
- pydub
- SMTP (Email Service)
- ZIP file handling

---

##  Web Service Workflow

1. User submits web form
2. Backend validates input
3. Mashup generated using the same logic as CLI
4. Output file compressed to ZIP
5. Email sent to user

---

## Exception Handling

The program handles:

- Incorrect argument count
- Invalid numeric inputs
- Insufficient video count
- Insufficient duration
- Download errors
- Audio processing errors
- File export failures

---



## Key Concepts Demonstrated

- Command line argument parsing
- YouTube data extraction
- Audio signal processing
- File system handling
- Exception handling
- Backend web development
- Email automation

---

## Conclusion

This assignment successfully demonstrates:

- Automation of multimedia processing  
- Integration of external libraries  
- Backend web service implementation  
- Robust validation and exception handling  

The Mashup Generator:

- Downloads multiple songs
- Converts to audio
- Extracts selected duration
- Merges into a single output
- Provides both CLI and Web interface

---

## Author

Kashish  
Roll Number: 102317186

---
