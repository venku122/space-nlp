
import spacy
import textacy.extract
import textacy.keyterms

# Load the large English NLP model
nlp = spacy.load('en_core_web_lg')

# The text we want to examine
text = """"
<Insert text on Saturn V here>
"""

# Parse the document with spaCy
doc = nlp(text)

# Extract semi-structured statements
statements = textacy.extract.semistructured_statements(doc, "Saturn V")

acronyms = textacy.extract.acronyms_and_definitions(doc)

quotations = textacy.extract.direct_quotations(doc)

namedEntities = textacy.extract.named_entities(doc)

keyTerms = textacy.keyterms.key_terms_from_semantic_network(doc)

# Print the results
print("Here are the things I know about Saturn V:")

for statement in statements:
    subject, verb, fact = statement
    print(' - {}'.format(fact))

print("Here are the acronyms and definitions I found about Saturn V:")

for acronym in acronyms:
    if acronyms[acronym] is not '':
      print(' - {}: {}'.format(acronym, acronyms[acronym]))

print("Here are the direct quoations I found about Saturn V:")

for quote in quotations:
    speaker, verb, quotation = quote
    print(' - {}: {}'.format(speaker, quotation))

# print("Here are the named entities I found about # Saturn V:")
# 
# for entity in namedEntities:
#     print(' - {}'.format(entity))

print("Here are the terms I found for Saturn V:")

for keyTerm in keyTerms:
    term, ranking = keyTerm
    print(' - {} rank: {}'.format(term, ranking))