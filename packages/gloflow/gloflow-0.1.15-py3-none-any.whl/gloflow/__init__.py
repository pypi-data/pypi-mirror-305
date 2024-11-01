




from gf_core import gf_core_sql_db
from gf_apps.gf_images.gf_images_client import gf_images_client
from gf_observe import gf_extern_load


print("gloflow...")


#-------------------------
# EXPORT_API
# simplified unified GF Py API with flattened namespace

# DB
db_init_client  = gf_core_sql_db.init_db_client
db_table_exists = gf_core_sql_db.table_exists

# IMAGES
add_image = gf_images_client.add_image

# OBSERVE
observe_ext_load = gf_extern_load.observe

T = gf_extern_load.T

#-------------------------
def run():
    print("gloflow.run()")
    True

