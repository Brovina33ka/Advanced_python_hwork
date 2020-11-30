#!/usr/bin/env python
# coding: utf-8

# In[16]:


from random import randint

class NucAcid:
    bases = {'A':'T','T':'A','U':'A','G':'C','C':'G'}
    
    def __init__(self, sequence: str):
        for letter in sequence:
            if letter not in self.bases:
                raise ValueError(f"This nuclear acid does not include base: {letter}")
                
        self.sequence = sequence

        
    def __add__(self, other):
        if type(other) == type(self):
            return type(self)(self.sequence + other.sequence)

    def __mul__(self, other):
        if type(self) != type(other):
            raise ValueError("incomparable types")
            
        new_sequence = ""
        
        for pair in zip(self.sequence, other.sequence):
            new_sequence += pair[randint(0, 1)]
        if len(self.sequence) > len(other.sequence):
            new_sequence += self.sequence[len(new_sequence):]
        else:
            new_sequence += other.sequence[len(new_sequence):]

        return type(self)(new_sequence)

    def __str__(self):
        raise NotImplementError

    def __getitem__(self, item):
        raise NotImplementError

    def __eq__(self, other):
        if type(self) == type(other):
            return self.sequence == other.sequence
        else:
            raise ValueError("incomparable types")

    def complementary_sequence(self):
        seq1 = ""
        for letter in self.sequence:
            seq1 += self.bases[letter]
        return seq1


class RNA(NucAcid):
    bases = {'A': 'T', 'U': 'A', 'G': 'C', 'C': 'G'}

    def __init__(self, sequence):
        super().__init__(sequence)
        
    def __str__(self):
        return self.sequence
    
    def __getitem__(self, item):
        return self.sequence[item]

    def complement(self):
        return Dna(self.complementary_sequence())


class DNA(NucAcid):
    bases = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

    def __init__(self, sequence):
        super().__init__(sequence)

    def __getitem__(self, item):
        return [self.sequence[item], self.bases[self.sequence[item]]]

    def __str__(self):
        return f"[{self.sequence}, {self.complementary_sequence()}]"


# In[ ]:




