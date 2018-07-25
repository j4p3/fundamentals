# This is the Scratch Pad. 
# The contents of this pad are synced to the other participants, but are not saved. 
# Use it ONLY for things you don't want saved in the CodePair report.Challenge: Write an in-memory, key-value value store that can "time travel."

# Basic operations
# You should be able to get and set values for arbitrary keys. In Ruby, this might look something like:

# kv = KV.new
# kv.set('foo', 'bar')
# kv.get('foo')
# =>  "bar"


# Advanced operations
# If a timestamp is provided for a given key, fetch the value for that key at that particular time.
# If no timestamp is supplied, fetch the most recently set value for that key. In Ruby, this might look like:

# kv = KV.new
# kv.set('foo', 'bar')
# now = Time.now.to_i
# sleep(1)
# kv.set('foo', 'bar2')

# # Fetch the key 'foo' with the 'now' timestamp
# kv.get('foo', now)
# => "bar"

# # Fetch the key 'foo' without a timestamp
# kv.get('foo')
# => "bar2" # returns the last set value


# Bonus points
# Support 'fuzzy' matching on a timestamp.

# kv = KV.new
# now = Time.now.to_i
# kv.set('foo', 'bar')
# sleep(3)
# kv.set('foo', 'bar2')

# Fetch the key 'foo' with the 'now' timestamp, plus 2 seconds
# kv.get('foo', now + 2)
# => "bar" # returns the closest set value to that timestamp, but always in the past

import time

COLORS = {
    'RED': 0,
    'BLACK': 1
}


class Node():
    def __init__(self, val):
        self.val = val
        self.color = COLORS['BLACK']
        self.p = None
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

    def insert(self, val):
        if val[0] <= self.val[0]:
            if not self.left:
                self.left = Node(val)
                self.left.p = self
                return self
            return self.left.insert(val)
        if not self.right:
            self.right = Node(val)
            self.right.p = self
            return self
        return self.right.insert(val)

    def search(self, timestamp_val):
        if self.val[0] == timestamp_val:
            return self

        if timestamp_val <= self.val[0]:
            if not self.left:
                return self
            return self.left.search(timestamp_val)
        if not self.right:
            return self
        return self.right.search(timestamp_val)


class Store():
    """
    Internal state:
    {
        'foo': [(<Timestamp>: 'bar')]
    }
    """

    def __init__(self):
        self._store = {}

    def set_value(self, key, value):
        current_time = time.time()
        timestamped_value = (current_time, value)

        if key not in self._store:
            self._store[key] = Node(timestamped_value)
        else:
            self._store[key].insert(timestamped_value)
        return timestamped_value

    def get_value(self, key, timestamp=None):
        values_list = self._store[key]
        if not timestamp:
            return values_list.maximum()
        else:
            return values_list.search(timestamp)


store = Store()
for i in range(10):
    store.set_value('foo', str(i)*3)
stored_value = store.set_value('foo', 'bar')
print(stored_value)
timestamp = stored_value[0] + 2
for i in range(10):
    store.set_value('foo', 'qux' + str(i))

# print(store._store)
print(store.get_value('foo', timestamp))
