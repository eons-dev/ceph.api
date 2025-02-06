import os
import logging
import apie
from flask import request

class create_user(apie.Endpoint):
	def __init__(this, name="Create Ceph User Endpoint"):
		super().__init__(name)

		this.supportedMethods = ['POST', 'PUT']
		this.mime = 'plain/text'
		this.clobberContent = False

		this.arg.kw.required.append('username')
		this.arg.kw.required.append('password')
		this.arg.kw.optional['email'] = None

	# Required Endpoint method. See that class for details.
	def GetHelpText(this):
		return '''\
Add a log message to the log aggregator.
'''

	def Call(this):
		
		# Adapted from https://github.com/canonical/microceph/blob/main/tests/scripts/actionutils.sh
		this.RunCommand(f"microceph.radosgw-admin user create --uid={this.username} --display-name={this.username} --email={this.email}")
		this.RunCommand(f"microceph.radosgw-admin key create --uid={this.username} --key-type=s3 --access-key {this.password} --secret-key Secret{this.password}")
		# FIXME: Improve key security
		
		this.response.code = 200
		this.response.content.string = "OK"
