# Copyright (c) 2013 Rackspace, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.

"""Exports SQLite driver controllers."""

from marconi.queues.storage.sqlite import catalogue
from marconi.queues.storage.sqlite import claims
from marconi.queues.storage.sqlite import messages
from marconi.queues.storage.sqlite import queues
from marconi.queues.storage.sqlite import shards


CatalogueController = catalogue.CatalogueController
ClaimController = claims.ClaimController
MessageController = messages.MessageController
QueueController = queues.QueueController
ShardsController = shards.ShardsController