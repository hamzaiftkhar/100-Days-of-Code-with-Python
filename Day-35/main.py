# Some Examples related to dictionary and sets concepts

programming_languages = {
    "Python": {
        "year_created": 1991,
        "creator": "Guido van Rossum",
        "paradigm": ["Object-Oriented", "Functional"],
        "popular_frameworks": ["Django", "Flask"]
    },
    "JavaScript": {
        "year_created": 1995,
        "creator": "Brendan Eich",
        "paradigm": ["Multi-paradigm"],
        "popular_frameworks": ["React", "Angular", "Vue"]
    }
}

print(programming_languages["Python"]["popular_frameworks"][0])

# Sets

programming_languages = {
    ("Python", {
        "year_created": 1991,
        "creator": "Guido van Rossum",
        "paradigm": {"Object-Oriented", "Functional"},
        "popular_frameworks": {"Django", "Flask"}
    }),
    ("JavaScript", {
        "year_created": 1995,
        "creator": "Brendan Eich",
        "paradigm": {"Multi-paradigm"},
        "popular_frameworks": {"React", "Angular", "Vue"}
    })
}


other_programming_languages = {
    ("C++", {
        "year_created": 1983,
        "creator": "Bjarne Stroustrup",
        "paradigm": {"Object-Oriented", "Procedural"},
        "popular_frameworks": {"Qt"}
    }),
    ("Java", {
        "year_created": 1995,
        "creator": "James Gosling",
        "paradigm": {"Object-Oriented"},
        "popular_frameworks": {"Spring", "Hibernate"}
    })
}

programming_languages.update(other_programming_languages)
