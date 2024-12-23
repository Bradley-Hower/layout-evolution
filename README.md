# Layout Evolution

## Summary

- Keyboard: **Corne Chocolate v2.0 (3x5)**
- Corpus: **British National Corpus (BNC) Baby Edition**
- Keyboard Analysis Tool: **Genkey**

Giving respect to Semilin. This project is a fork of Semilin's project. https://semilin.github.io/genkey/

The project was inspired by adumb's video. https://www.youtube.com/watch?v=EOaPb9wrgDY

## Keyboard

The question of how many keys is enough and how many is too many is of great interest. Ben Vallack has some great videos where he explores the extremes of minimalism in a keyboard. https://www.youtube.com/@BenVallack Utlimately, while layers are a great hack for efficiency, over doing them can turn into an encumbrance. Using 15 keys for each hands group of four fingers (six for the index finger, the remaining fingers each are assigned to three) is widely considered the most practical. For thumbs, however, some opt for two keys each, while others use three. For this project, three each will be used. The rationale being, while two each can be used, the awkward and heavier usage of key combos makes it less preferred. In total, 36 keys in a split keyboard, a split keyboard being the most comfortable and offering more freedom of movement.

The keyboard chosen for this project is the Corne Chocolate v2.0 keyboard. This keyboard uses low-profile Kailh choc v1 switches. There are other brands of switches on the market which can be used.

[Corne Keyboard Image]

https://github.com/foostan/crkbd/blob/main/docs/corne-chocolate/v2/buildguide_en.md

Reasons this keyboard was chosen:

- Low-profile option.
- Vertically aligned key columns.
- Column staggering to fit the natural arch of hands.
- Minimal keys.
- Split keyboard.

These reasons are very sensible. However, why vertical alignment of the columns? Ben Vallack also has an interesting video where he explores this question. https://www.youtube.com/watch?v=1C2bJkzIaPE In short, the opening and closing of hands naturally fits well to this alignment.

## Corpus

For Power Layout, the British National Corpus (BNC) was chosen as the source of character analysis.

https://www.english-corpora.org/bnc/

Complete

https://llds.ling-phil.ox.ac.uk/llds/xmlui/handle/20.500.14106/2554

Baby Edition

https://llds.ling-phil.ox.ac.uk/llds/xmlui/handle/20.500.14106/2553

This corpus was chosen for a number of reasons. For one, Oxford University Press is largely considered the leading authority on the English language. This means that quality sources would be used for purposes of the analysis. Two, with the intentions of creating a keyboard layout for all forms and purposes, it was seen as of best interest to choose a corpus that encompasses various genres, which BNC does indeed do. Lastly, while many would argue that more of our modern usage of English is in new forms, such as coding, informal online text, and direct messaging, these forms are not to be taken with serious considerations.

For the sake of time, the Baby Edition of BNC was used.

With creating a layout there are some serious philosophical considerations that need to be taken into consideration. While it is easy to say we should design the layout to fit contemporary usage, this can be seen as a flaw for a number of reasons.

1. **Keyboard Layouts are Very Durable** Layouts have proven to be very immune to change as they are very difficult to adapt. Any individual learning to type must undertake considerable amounts of practice to be proficient. Thus, while the current subculture of keyboards and keyboard layouts is experimental, it is foreseeable that some day a stable keyboard layout will be acquired into the mainstream due to prodigious ease of use and efficiency. Thus, much consideration should be given to choosing a layout that is innately durable.

2. **The Language Meets the Medium** It is of serious consequence the tools that are chosen to complete a task. What chisel to use to carve stone, the writing implement for writing prose, the keyboard for which a statement is made. Any serious professional will tell you that their tools are very important for implementing a goal or vision. And yes, while many forms of tools *can* work, when people are faced with realities of work, the incentives can be rather discouraging. One would not be expected to be so willing to dig a trench with a spoon after all. And a relatively recent parallel can be drawn very easily. The feature phone. While, yes, one can write anything using the 12-key layout, the motivations result in otherwise. This resulted in a brief period where the English language was being bastardized with the likes of "LOL" and "BRB". Acronyms were run amuck. And people were much more terse in speech. If a keyboard layout is designed for coding or informal language, people will be disincentivized to used formal language.

3. **Aspirations** With it now in mind that a layout should be durable and good, that leaves us with the question, "What is good?". In this case I think it best to refer to authority, to the most literate and well-read among us, presumably. By using sources compiled by those of great recognition, curating a collection of works that are considered of fine composition, we will have as closely come to "good" as can be objectively achieved. Thus, by creating a layout that best fits this form of English, we best encourage this quality level of composition.

4. **Omissions** Many would say that for the number of hours spent in a day, they mostly use keyboards for writing code. Some individuals have even keylogged themselves and shown that due to using a coding language, such as Java, the total key usage is heavily biased in a different direction, with much more emphasis on brackets, punctuation, and symbols. And while this argument is enticing, there are some great failures in the reasoning. For one, coding languages rarely last more than a decade or two. Graveyards are filled with dead coding languages. It is exceptionally rare for a coding language to survive and even less common to remain in common usage. All coding language are evolving and in no small ways. Furthermore, the recent bounds made with AI and predictive-text has proven that the foundation of coding and coding practices is anything but stable.

## Assigning Keys to Layers

To determine which keys should be set to each layer, this project uses NLTK to run key frequency analysis. NLTK has a great module which allows for easier use of the BNC XML source mentioned earlier. Further, one is able to sort words pulled from a corpus and run analysis. https://github.com/nltk/nltk

With this analysis, key frequency was determined and sorted into "results_value_sorted.txt". Notice, backtick '`' only occurred once and five other characters ('^', '~', '@', '#', '\'), not at all. There is no doubt that these characters are indeed more rare, but once or zero in 3.5 million words leaves doubts. The full BNC corpus had similar results while having 100 million words, indicating a lack of representation. Looking at the other symbols, we see lackwise lacking representation. Certainly symbols are not common in classic English literature, but some better representation (although unclear how best achieved) needs to be had. In follow-up work to this, other corpuses will be explored and analyzed to find better representation of rarer characters.

For those interested in running their own key frequency analysis, see the "Key Analysis" folder. If you have downloaded the BNC, running this code will also create a text file version of the corpus, useful for later keyboard analysis. This text file will need to be opened and re-saved as a text file within a text-file editor due to encoding issues. LibreOffice Writer has proven to be effective. Sufficient memory will be needed to handle the heavy load. Lines have been clearly marked in the code if you are not interested in creating the text file copy.

### Steps Taken to Set Layers

How to set the layers was a bit fuzzy to start. What is more important, keeping like-characters together? Or adhering striclty to statistics? Fortunatley, which side to push characters became apparent once looking into the matters.

1. Assignment begins with the following:

- Letters to Layer 1
- Capital letters to Layer 2
- Numbers to Layer 3
- The following to Layer 3 for conveniences due to usefullness with numbers:

```
←
→
↑
↓
Home
End
-
^
(
)
>
<
*
$
%
/
=
+
```

*The  carrot '^' key was not in the key analysis results.

Characters remaining:

[Layer 0]

2. This leaves the following to be assigned. Layer 1, 2, and 3 need four, four, and two additional characters respectively. Each are added according to frequency.

Character Assignments:
[Layer 0-2]

After Assignment:
Layer 1
[Layer 1]

Layer 2
[Layer 2]

3. On Layer 3, to keep the brackets and curly brackets together, they will be moved together to Layer 4. Adding the pipe instead finishes off Layer 3.
[Layer 3]

4. With the remaining characters added to Layer 4, remainung missing characters need to be added. The remaining missing characters are '~', '@', '#', and '\'.
[Layer 4]

### Additional keys of interest

The following lists are some keys if interest that might be added to Layer 4.

- Escape
- Mute
- Volume Down
- Volume Up
---
- Function
- Menu
- Print screen
- Lock
---
- Brightness up
- Brightness down

Additional Bonus Symbols:

- Em dash '—'
- Degree '°'
- Bullet '•'
- Copyright '©'

## Method

****
Evolution model

- Selecting top ten to go forward
- Mutating the top 30% for possibility to go forward

This approach ensures greater breadth so that a layout has a chance to evolve into better standing.
****





## Analysis of Layouts

Each layout is scored by Genkey. Genkey offers some great customization, including weighting for fingers based on strength.

### From Source

If you wish to build from source, visit the genkey website:

https://semilin.github.io/genkey/

Here is a great guide on setting up Go for that purpose:

https://www.redswitches.com/blog/how-to-install-go-on-debian/

## Run

This program requires Python to be installed to run. To initiate a run, execute the "run.py" file within Python.

Note: To use a txt file corpus, move it to the main folder and load. `./genkey load corpusfilename` After loading, this file name needs to be present at the top of the config file.

### Continued Reading

- Interesting (although somewhat verbose) document on layouts: https://docs.google.com/document/d/1Ic-h8UxGe5-Q0bPuYNgE3NoWiI8ekeadvSQ5YysrwII/edit#heading=h.p43k42hc1wc2