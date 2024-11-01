# Hirsch 🦌
Python implementation of the familiar discrete Hirsch index (h-index) from academic writing, with an abstracted continuous version for use as a statistical measure of even distribution

## Installation

```
pip install hirsch
```

## Usage

### Discrete

Get the h-index of some discrete data, e.g. the number of citations an author has received on their papers:

```
from hirsch import hirsch
citations = [0, 1, 1, 2, 1, 6, 5, 13, 14, 10, 59, 145, 68]
h = hirsch(citations)
```
![discrete](https://github.com/user-attachments/assets/7e68faed-53b0-4f09-8c32-18ba9d6dc62d)

### Continuous

Calculate a continuous h-index for some normalised and binned data, e.g. fractional populations:

```
from hirsch import hirsch
fractions = [0.1,0.5,0.6,0.3,0.2,0.5,0.4]
h = hirsch(fractions, continuous=True)
```
![continuous](https://github.com/user-attachments/assets/5627e6c6-ac3a-4bdf-b069-b38d233d5aed)

Calculate a continuous h-index for a set of samples from known populations (continuous=True assumed):

```
from hirsch import hirsch
samples = [1,2,3,4,10,20,10]
populations = [10,10,10,10,20,30,40]
h = hirsch(samples, populations)
```
