# CTF Decoder – Python Decoding Challenges

## About the Project

CTF Decoder is one of my early Python projects, created to practice programming fundamentals through a series of decoding challenges inspired by Capture The Flag (CTF) exercises.

The project includes 10 levels, each involving different encoding formats or data transformations.

The first 9 levels contain implemented solutions, while Level 10 is still a work in progress.

This repository documents my learning process and experimentation with Python.

## Techniques Explored

- **Level 1:** Hexadecimal decoding
- **Level 2:** Base64 decoding and integer-to-bytes conversion
- **Level 3:** Base64 and hexadecimal decoding
- **Level 4:** Repeated Base64 decoding
- **Level 5:** Hexadecimal decoding and byte reversal
- **Level 6:** UTF-16 Big Endian decoding
- **Level 7:** Multiple decoding layers (hexadecimal and Base64)
- **Level 8:** Processing mixed hexadecimal and Base64 segments
- **Level 9:** Base64 decoding and character transformation
- **Level 10:** Initial exploration of binary data and XOR operations (incomplete)

## Technologies Used

- Python 3
- `base64` module
- Built-in Python functions for byte and string manipulation

## How to Run

Clone the repository:

```bash
git clone https://github.com/marcogia1512/CTF_Decoder.git
cd CTF_Decoder
```

Run the Python script:

```bash
python ctf_decoder.py
```

**Note:** In the current version, the script executes the experimental Level 10 function. To display the results of Levels 1–9, comment out the standalone `solve_level_10()` call and uncomment `main()` at the bottom of the file.

## What I Learned

Through this project, I practiced:

- Writing and organizing Python functions
- Working with strings, bytes, and character encodings
- Using Python's Base64 module
- Applying multiple decoding operations
- Solving problems through experimentation and logical reasoning

## Current Limitations

- Level 10 is incomplete.
- The program uses predefined challenge inputs rather than accepting arbitrary user input.
- Some decoding operations assume that the input is correctly formatted.
- The project is an educational exercise, not a general-purpose decoding tool.

## Future Improvements

- Complete Level 10
- Improve code organization and execution flow
- Add error handling
- Allow users to select individual levels
- Add automated tests

## Learning Journey

This repository represents an early stage of my Python and cybersecurity learning journey.

My goal is to continue improving my programming and problem-solving skills through hands-on projects and security-related exercises.
