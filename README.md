
[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/cc-0.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)


# Table of Contents

1. [Introduction](#introduction)
2. [Steps to Contribution](#contributing-guidelines)
3. [Introduction to Python](#introduction-to-python)
4. [Introduction to Kivy](#introduction-to-kivy)
5. [About the Game](#about-the-game)
6. [File Structure](#file-structure)
7. [Issue Listing](#issue-listing)
8. [Conclusion](#conclusion)

# Introduction

Welcome to the open-source project, **Octops**! In Octops, we've combined the nostalgia of the original game **Counter Strike 1.6** with an exciting new gameplay concept.
If you're eager to dive into the action and defuse the bomb, follow this documentation to set up and play the game. We'll guide you through the installation process and provide all the necessary information to get you started.

# Steps to Contribution

## Fork the Repository

Fork this repository by clicking on the `Fork` button on the top of this page. This will create a copy of this repository in your account.

<img align="right" width="300" src="https://github.com/MLSAKIIT/first-contributions/blob/main/.github/assets/README/fork.png" alt="Fork the Repository"/>

---

## Clone the Repository

Clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the `Code` button and then click the `Copy to Clipboard` icon.

<img align="right" width="300" src="https://github.com/MSCKIIT/first-contributions/blob/main/.github/assets/README/clone.png" alt="Clone the Repository"/>

Open a terminal and run the following git command:

```
git clone https://github.com/<your_username>/octops.git
```

<img align="right" width="300" src="https://github.com/MLSAKIIT/first-contributions/blob/main/.github/assets/README/copy-url.png" alt="Copy URL to Clipboard"/>

---
## Create a Branch

Change to the repository directory on your computer (if you are not already there):

```
cd octops
```

Now create a branch using the `git checkout` command:

```
git checkout -b <your-new-branch-name>
```

For example:

```
git checkout -b 2201001-paarth
```

The name of the branch does not need to have the word _add_ in it, but it's a reasonable thing to include because the purpose of this branch is to add your name to a list.

---

## Make Necessary Changes and Commit the Changes

If you go to the project directory and execute the command `git status`, you'll see there are changes.

Add those changes to the branch you just created using the `git add -A` command:

Now commit those changes using the `git commit` command:

```
git commit -m "Issue <Number>, <Name>, <Description of your changes>"
```

By replacing `<Name>` with your full name.
and `<Number>` as displayed on the `<issues>` tab of the GitHub repo    


## Push Changes to GitHub

Push your changes using the command `git push`:

```
git push origin <add-your-branch-name>
```

By replacing `<add-your-branch-name>` with the name of the branch you created earlier.

---

## Submit Your Changes for Review

If you go to your repository on GitHub, you'll see a `Compare & pull request` button. Click on that button.

Now submit the pull request.

Soon all your changes will be merged into the master branch of this project. You will also get a notification e-mail once the changes have been merged.

---

## Where to Go from Here?

Congrats! You just completed the standard _fork -> clone -> edit -> pull request_ workflow that you'll encounter often as a contributor.

---

# Introduction to Python

This is the second section of your document.

# Introduction to Kivy

Kivy is an open-source Python library for developing multi-touch applications. It's designed to be highly flexible, cross-platform (Windows, macOS, Linux, Android, and iOS), and user-friendly. Kivy allows you to create beautiful and interactive user interfaces for a wide range of applications, from simple desktop programs to mobile apps.

## Using .kv Files

One of Kivy's standout features is its use of .kv files for declarative user interface design. .kv files are simple text files that describe the structure and behavior of your application's widgets and UI. This separation of UI from code makes it easy to design and maintain complex user interfaces. To use .kv files, you need to:

1. Name your .kv file with a similar name as your Python file (e.g., `main.py` and `main.kv`).
2. Load the .kv file using the `Builder` class and the `load_file()` method.

Here's a basic example of a .kv file:

```kv
<MyWidget>:
    Button:
        text: "Click Me"
        on_release: root.button_pressed()
```

## Widgets

Kivy provides a wide range of widgets to build your user interface. Here are some common widgets and their parameters:

### Layouts

Layouts in Kivy are specialized widgets that are used to arrange and organize other widgets within your user interface. They help you define the structure and positioning of various UI elements in your application

#### BoxLayout

- **orientation**: The orientation of the layout (either 'horizontal' or 'vertical').
- **spacing**: The space between widgets on the layout.

```kv
BoxLayout:
    orientation: 'horizontal'
    spacing: 10
    Button:
        text: 'Button 1'
    Button:
        text: 'Button 2'
```

#### FloatLayout

- **size_hint**: The widget's size relative to the layout's size.
- **pos_hint**: The widget's position within its parent layout or window. `center_x` and `center_y` take values between 0 and 1 where `(0.5, 0.5)` is the absolute center of the layout.

```kv
FloatLayout:
    Button:
        size_hint: 0.2, 0.2
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
```

### Label

The Label widget in Kivy is used to display text or simple static content within your application. It's a fundamental widget for providing information, instructions, or identifying elements in the user interface.

- **text**: Specifies the text content to be displayed within the label.
- **font_size**: Sets the font size for the text.
- **size**: Defines the size of the label based on its content.

```kv
Label:
    text: "Welcome to Kivy!"
    font_size: '24sp'
    size: self.texture_size
```

### Button

- **Text**: The text displayed on the button.
- **on_release**: An event that gets triggered when the button is released.
- **on_press**: Calls a function when button is pressed
- **disabled**: Controls whether button will remain enabled/disabled. Can be controlled by conditions
- **size**: Sets the dimensions of the widget. `dp` parameter on the dimensions refers to density-independent pixels which are used to ensure consistent sizing across different devices.

```kv
Button:
    text: "Click Me"
    size: dp(147), dp(61)
    on_release: root.button_released()
    on_press: root.change_image()
    disabled: True if bg_img.opacity == 0 else False
```

### Image

- **id** - Used to tag the specific widget/component to access it somewhere else in the program
- **source**: The path to the image file to be displayed.
- **opacity**: Changes the opacity of the image

```kv
Image:
    id: my_image
    source: 'my_image.png'
    opacity: 0.5
```

### Slider

- **Value**: The current value of the slider.
- **min**: The minimum value of the slider.
- **max**: The maximum value of the slider.
- **on_value**: Calls a function when slider value changes

```kv
Slider:
    value: 50
    min: 0
    max: 100
    on_value: root.slider_val_change()
```

These are just a few examples of the many widgets and parameters available in Kivy. Refer to the official Kivy documentation for a comprehensive list of widgets and their attributes: [Kivy Widgets](https://kivy.org/doc/stable/api-kivy.uix.html)

## Kivy Classes

Kivy classes are a fundamental part of the Kivy framework, designed to help developers build user interfaces and interactive cross-platform applications more efficiently. Some classes and methods used in our app are as follows:

### Screen

The `Screen` class in Kivy is used for creating distinct screens or views within a Kivy application. The `ScreenManager` is often used to manage and switch between different screens. They are a fundamental component for creating navigation flows and separating different parts of an app's user interface.

### SoundLoader

The `SoundLoader` class in Kivy is a utility class that allows you to load and manage audio files(e.g., MP3, WAV) within your Kivy application. You can use `SoundLoader` to load sound files, set volume levels, play, pause, or stop sounds, and manage audio resources efficiently.

### Clock

The `Clock` class in Kivy is a central part of the Kivy framework which provides a mechanism for scheduling functions to run at specific intervals or after a delay. The `Clock` class is useful for implementing animations, updating UI elements, and performing tasks that require precise timing.

Kivy's flexibility and ease of use make it a powerful tool for creating interactive and visually appealing user interfaces in Python. Explore the documentation and start building your own Kivy applications today!

# About the Game

The game consists of different screens based on Counter Strike 1.6 theme. There's a map which gives access to different locations. Each screen presents players with a distinct challenge or mission. There are hints which can be located on the bomb. To succeed, players must solve puzzles, and apply their skills effectively. Once all the tasks are accomplished, players gain access to the bomb and must defuse it to win the round.


# File Structure

The project is structured into several folders and files:

### 1. **assets/**

The `assets/` directory is intended for storing assets such as images, fonts, audio, and other resources that your application may need. These assets can be accessed within your Kivy files.

Example:
- `assets/main_logo.png`

### 2. **screen_layout/**

The `screen_layout/` directory contains the Kivy language (KV) files that define the structure and appearance of the app's screens and their layouts. These KV files are built to their respective screens in the `screens/` folder using `Builder.load_file()`.

Example:
- `screen_layout/main_screen.kv`
- `screen_layout/map_screen.kv`

### 3. **screens/**

The `screens/` directory is intended for Python files that define the behavior and logic of individual screens within your application. These screens are managed and coordinated using Kivy's `ScreenManager` in the main Python file.

Example:
- `screens/main_screen.py`
- `screens/map_screen.py`

### 4. **octops.py**

`octops.py` is the main Python script that acts as the entry point of your Kivy application. It connects and manages all the components of your application, including screens, transitions, and user interactions. This script initializes the Kivy app and sets up the screen manager.

Example:
- `octops.py`

## How It Works

1. The `octops.py` script is the entry point of the application. It initializes the Kivy app and sets up the screen manager.

2. The KV files in the `screen_layout/` directory define the layout and appearance of the screens and widgets.

3. The Python files in the `screens/` directory define the behavior and logic of individual screens. These screens are built to the corresponding KV files.

4. The `ScreenManager` in `octops.py` manages transitions between different screens based application logic.

## Getting Started

To run the Octops Kivy app on your local machine, follow these steps:

1. Clone the repository to your local machine:

   ```sh
   git clone https://github.com/Afterdie/octops-final
   ```

2. Install the required dependencies if you haven't already. You may use a virtual environment for this:

   ```sh
   pip install kivy
   ```

3. Navigate to the project directory:

   ```sh
   cd octops-final
   ```

4. Run the application:

   ```sh
   python octops.py
   ```

The app should launch, and you can interact with it to explore its functionality.

# Issue Listing

This is the second section of your document.

# Conclusion

Thank you for being part of our community, and we look forward to sharing countless thrilling moments as we defuse bombs and tackle new challenges together!
