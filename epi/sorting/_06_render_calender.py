import collections

Event = collections.namedtuple("Event", ("start", "end"))
Endpoint = collections.namedtuple("Endpoint", ('time', 'is_start'))

def find_max_simultaneous_events(arr):
    E = []
    for event in arr:
        E.append(Endpoint(event.start, True))
        E.append(Endpoint(event.end, False))
    
    # not e.is_start because False comes before True when sorting (incase of ties)
    E.sort(key = lambda e:(e.time, not e.is_start))
    max_simultaneous_events = 0
    num_simultaneous_events = 0
    for e in E:        
        if e.is_start:
            num_simultaneous_events += 1
            max_simultaneous_events = max(max_simultaneous_events, num_simultaneous_events)
        else:
            num_simultaneous_events -= 1
        #print e.time, e.is_start, max_simultaneous_events
    return max_simultaneous_events

if __name__ == "__main__":
    arr = [
        Event(1,5), Event(6,10), Event(11,13), Event(14,15),
        Event(2,7), Event(8,9), Event(12,15),
        Event(4,5), Event(9,17)
    ]
    print "Max simultaneous events =", find_max_simultaneous_events(arr)