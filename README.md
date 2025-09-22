# 📚 Flashy – French Vocabulary Flashcards  

🚀 This project was built on **Day 31 of my Python Bootcamp**.  
It’s a fun and interactive flashcard app that helps you learn **French to English vocabulary** using Python and Tkinter.  

---

## 🌟 Features  
- 🎴 **Flashcards** show a random French word.  
- ⏳ After 3 seconds, the card **flips** to reveal the English translation.  
- ✅ **“Known” button**: removes the word from the learning list and saves your progress.  
- ❓ **“Unknown” button**: skips the current card and shows a new one.  
- 💾 Progress is saved in a CSV file so you don’t lose your learning state.  

---

## 🛠️ How it Works  
1. 📂 The program first tries to load `words_to_learn.csv` (your personal progress file).  
   - If it doesn’t exist, it falls back to the default `french_words.csv`.  
2. 🎲 A **random word** is chosen and displayed in French.  
3. ⏳ After 3 seconds, the flashcard **flips** to show the English meaning.  
4. ✅ Clicking “Known” removes the word from your learning list and updates the CSV.  
5. 🔁 The cycle continues until you’ve gone through all words!  

---

## 🖥️ Tech Stack  
- 🐍 **Python**  
- 🖼️ **Tkinter** (for GUI)  
- 📊 **Pandas** (for handling CSV data)  

---

## 🎨 UI Setup  
- 🖼️ Uses **card images** (`card_front.png`, `card_back.png`) to simulate flashcards.  
- 🔘 Buttons with ✅ and ❌ icons for user interactions.  
- 🎨 Clean canvas with text overlays for **language** and **word display**.  

---

## 📂 Project Structure  
```
📁 data  
 ┣ 📄 french_words.csv      # Default vocabulary file  
 ┣ 📄 words_to_learn.csv    # User progress file (auto-generated)  

📁 images  
 ┣ 🖼️ card_front.png  
 ┣ 🖼️ card_back.png  
 ┣ 🖼️ right.png  
 ┗ 🖼️ wrong.png  

```



## 🎯 What I Learned  
- How to use **Tkinter canvas** for displaying images & text.  
- How to manage **time delays** and card flipping using `window.after`.  
- Handling **CSV files with Pandas** to save progress.  
- Error handling with `try/except` for missing files.  

---

✨ This project was a big step in practicing **Python GUI development** and making learning French more fun!  
