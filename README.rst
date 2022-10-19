Serlo Bot
=========

The class `SerloBot <./serlo/bot.py>`_ helps in updating https://serlo.org/. This class is used in different `Jupyter notebooks <./notebooks>`_ to maintain serlo.org (e.g. delete bots, correct links, etc.).

The `Bot for changing revisions <./notebooks/2022-10-19-Bot_for_changing_revisions.ipynb>` is there to automatically search all entities and perform changes on them (e.g. delete all empty boxes). It uses the `helper_functions.ipynb ./notebooks/helper_functions.ipynb` and all files containig changing rules (e.g `boxes.ipynb <./notebooks/boxes.ipynb`)
In get_potential_entites_to_be_updated() we look in a local database dump for entities having a pattern to be updated. Then in get_newest_unrevised_revision() we get all the entities we want to change from the API (Staging or Production). With apply_rules() the changes are executed and after that sent to the API.
All changes made need a review.
