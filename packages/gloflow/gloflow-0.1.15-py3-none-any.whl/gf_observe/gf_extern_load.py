# GloFlow application and media management/publishing platform
# Copyright (C) 2024 Ivan Trajkovic
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""
extern_load 
	- helps with tracking and monitoring of external data loading.
	- tracks loads of external data as events in the DB.
	- allows for historic tracking of external data loading.
	- simple mechanism, py native.
	- results of loads are stored in the DB in string form
		- results can be html or json.
		- if json then stored in postgres jsonb type.
	- the partition key is stored for each load event.
		- parititon keys can be multidimensional
		- each dim separated by "__".
"""

import json
import gloflow as gf

# stores data on loading/processing of external models info
# such as from automani or some other source.
table_name__extern_load_str = "gf_vehicles_extern_load"

#---------------------------------------------------------------------------------
# OBSERVE
def observe(p_load_type_str,
	p_part_key_str,
	p_source_domain_str,
	p_runtime_map,
	p_meta_map={},
	p_url_str=None,
	p_resp_type_str="json",
	p_resp_data_html_str=None,
	p_resp_data_json_map=None):
	
	assert(isinstance(p_load_type_str, str))
	assert(p_resp_type_str == "html" or p_resp_type_str == "json")
	if p_resp_type_str == "json":
		assert(isinstance(p_resp_data_json_map, dict))

	id_str = db_insert(p_load_type_str,
		p_part_key_str,
		p_source_domain_str,
		p_runtime_map["db_client"],
		p_meta_map,
		p_url_str)

	db_update_response(id_str,
		p_resp_type_str,
		p_runtime_map["db_client"],
		p_resp_data_html_str=p_resp_data_html_str,
		p_resp_data_json_map=p_resp_data_json_map)
	
#---------------------------------------------------------------------------------
# DB
#---------------------------------------------------------------------------------
def db_insert(p_load_type_str,
	p_part_key_str,
	p_source_domain_str,
	p_db_client,
	p_meta_map={},
	p_url_str=None):
	assert(isinstance(p_meta_map, dict))

	cur = p_db_client.cursor()

	query_str = f'''INSERT INTO {table_name__extern_load_str} (
			load_type,
			part_key,
			url,
			meta_map,
			source_domain
		)
		VALUES (%s, %s, %s, %s, %s)
		RETURNING id
	'''

	cur.execute(query_str, 
		(
			p_load_type_str,
			p_part_key_str,
			p_url_str,
			json.dumps(p_meta_map),
			p_source_domain_str
		))

	id_int = cur.fetchone()[0]
	p_db_client.commit()
	cur.close()

#---------------------------------------------------------------------------------
def db_update_response(p_id_int,
	p_resp_type_str,
	p_db_client,
	p_resp_data_html_str=None,
	p_resp_data_json_map=None):
	
	if not p_resp_data_json_map is None:
		assert(isinstance(p_resp_data_json_map, dict))
	else:
		assert(isinstance(p_resp_data_html_str, str))

	cur = p_db_client.cursor()

	query_str = f'''
		UPDATE {table_name__extern_load_str}
		SET
			resp_type = %s,
			resp_data_html = %s,
			resp_data_json = %s

		WHERE id = %s
	'''

	cur.execute(query_str, (
		p_resp_type_str,
		p_resp_data_html_str,
		p_resp_data_json_map,
		p_id_int
	))
	p_db_client.commit()
	cur.close()

#---------------------------------------------------------------------------------
def db_init(p_db_client):

	cur = p_db_client.cursor()
	
	if not gf.db_table_exists(table_name__extern_load_str, cur):
		
		# source_domain  - domain on which this ad was discovered
		# fetch_datetime - time when the GF system stored this item

		sql_str = f"""
			CREATE TABLE {table_name__extern_load_str} (
			
				id SERIAL PRIMARY KEY,
				
				-- what type of extern loading is done
				-- model, model_variant, etc.
				load_type VARCHAR(255),

				-- -----------------------
				-- PARTITION_KEY
				-- string representing partition key
				part_key VARCHAR(255),

				-- -----------------------
				-- for html data this is the URL of the page, for json
				-- returns it might be the URL of the API endpoint.
				-- for other types of data it might be None.

				url VARCHAR(1000),
				
				-- -----------------------
				-- RESPONSE
				-- coming from the external source, can be html, json, etc.
				resp_type      VARCHAR(255),
				resp_data_html TEXT,
				resp_data_json JSONB,

				-- -----------------------
				-- META
				-- various metadata that can be attached to a load event.
				meta_map JSONB,
				
				-- -----------------------

				source_domain  VARCHAR(255),
				fetch_datetime TIMESTAMP DEFAULT NOW()
			);
		"""
		cur.execute(sql_str)
		p_db_client.commit()