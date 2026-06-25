from printing_functions import *
from printing_functions import print_models
from printing_functions import show_completed_models as scm

completed_models = ["toyota", "subaru", "arigato", "gozaimasu", "nagasaki"]
imcompleted_models = []


print_models(completed_models, imcompleted_models)
scm(imcompleted_models)
