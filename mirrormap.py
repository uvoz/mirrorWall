# The MIRROR MAP
# 2019 by StrejcekBob
# Upgraded by MakerMatty
# Tested by MakerMatty
# This file contains the Mirror map that enables us to retrieve the hub, bonnet and the i2cports for a given mirror.
# Mirrormapping serves sofware & people that wish to operate mirrors based on their logical ID.

# funtions exposed:

# getMirrorAddress(mirror)
# returns a complete record for a mirror  : e.g. {"mirror":0,"mirror_hub":0,"hub":2,"bonnet":1,"UD-port":0,"LR-port":1}
# Sample code:
# import mirrormap as mm
# address=mm.getMirrorAddress(1)
# print(address['bonnet'])

# getMirroHub(mirror)      -returns the hub ID the mirror belongs to: e.g. 2
# Sample code:
# import mirrormap as mm
# print(mm.getMirroHub(2))
# would return 3

hubmappings={
"hub1":[
{"mirror_hub":0,"mirror":44,"hub":1,"bonnet":0,"UD-port":0,"LR-port":1},
{"mirror_hub":1,"mirror":43,"hub":1,"bonnet":0,"UD-port":2,"LR-port":3},
{"mirror_hub":2,"mirror":54,"hub":1,"bonnet":0,"UD-port":6,"LR-port":7},
{"mirror_hub":3,"mirror":42,"hub":1,"bonnet":0,"UD-port":4,"LR-port":5},
{"mirror_hub":4,"mirror":53,"hub":1,"bonnet":0,"UD-port":8,"LR-port":9},
{"mirror_hub":4,"mirror":53,"hub":1,"bonnet":0,"UD-port":8,"LR-port":9},
{"mirror_hub":5,"mirror":63,"hub":1,"bonnet":2,"UD-port":4,"LR-port":5},
{"mirror_hub":6,"mirror":41,"hub":1,"bonnet":1,"UD-port":6,"LR-port":7},
{"mirror_hub":7,"mirror":52,"hub":1,"bonnet":1,"UD-port":8,"LR-port":9},
{"mirror_hub":8,"mirror":62,"hub":1,"bonnet":2,"UD-port":8,"LR-port":9},
{"mirror_hub":9,"mirror":71,"hub":1,"bonnet":2,"UD-port":2,"LR-port":3},
{"mirror_hub":10,"mirror":40,"hub":1,"bonnet":1,"UD-port":0,"LR-port":1},
{"mirror_hub":11,"mirror":51,"hub":1,"bonnet":1,"UD-port":2,"LR-port":3},
{"mirror_hub":12,"mirror":61,"hub":1,"bonnet":1,"UD-port":4,"LR-port":5},
{"mirror_hub":13,"mirror":70,"hub":1,"bonnet":2,"UD-port":6,"LR-port":7},
{"mirror_hub":14,"mirror":78,"hub":1,"bonnet":2,"UD-port":0,"LR-port":1}
],

"hub2":[
{"mirror":34,"mirror_hub":0,"hub":2,"bonnet":0,"UD-port":0,"LR-port":1},
{"mirror":24,"mirror_hub":1,"hub":2,"bonnet":0,"UD-port":2,"LR-port":3},
{"mirror":33,"mirror_hub":2,"hub":2,"bonnet":0,"UD-port":6,"LR-port":7},
{"mirror":15,"mirror_hub":3,"hub":2,"bonnet":0,"UD-port":4,"LR-port":5},
{"mirror":23,"mirror_hub":4,"hub":2,"bonnet":0,"UD-port":8,"LR-port":9},
{"mirror":32,"mirror_hub":5,"hub":2,"bonnet":2,"UD-port":4,"LR-port":5},
{"mirror":7,"mirror_hub":6,"hub":2,"bonnet":1,"UD-port":6,"LR-port":7},
{"mirror":14,"mirror_hub":7,"hub":2,"bonnet":1,"UD-port":8,"LR-port":9},
{"mirror":22,"mirror_hub":8,"hub":2,"bonnet":2,"UD-port":8,"LR-port":9},
{"mirror":31,"mirror_hub":9,"hub":2,"bonnet":2,"UD-port":2,"LR-port":3},
{"mirror":0,"mirror_hub":10,"hub":2,"bonnet":1,"UD-port":0,"LR-port":1},
{"mirror":6,"mirror_hub":11,"hub":2,"bonnet":1,"UD-port":2,"LR-port":3},
{"mirror":13,"mirror_hub":12,"hub":2,"bonnet":1,"UD-port":4,"LR-port":5},
{"mirror":21,"mirror_hub":13,"hub":2,"bonnet":2,"UD-port":6,"LR-port":7},
{"mirror":30,"mirror_hub":14,"hub":2,"bonnet":2,"UD-port":0,"LR-port":1},
{"mirror":45,"mirror_hub":15,"hub":2,"bonnet":0,"UD-port":10,"LR-port":11}
],


"hub3":[
{"mirror":35,"mirror_hub":0,"hub":3,"bonnet":0,"UD-port":0,"LR-port":1},
{"mirror":26,"mirror_hub":1,"hub":3,"bonnet":0,"UD-port":2,"LR-port":3},
{"mirror":25,"mirror_hub":2,"hub":3,"bonnet":0,"UD-port":6,"LR-port":7},
{"mirror":18,"mirror_hub":3,"hub":3,"bonnet":0,"UD-port":4,"LR-port":5},
{"mirror":17,"mirror_hub":4,"hub":3,"bonnet":0,"UD-port":8,"LR-port":9},
{"mirror":16,"mirror_hub":5,"hub":3,"bonnet":2,"UD-port":4,"LR-port":5},
{"mirror":11,"mirror_hub":6,"hub":3,"bonnet":1,"UD-port":6,"LR-port":7},
{"mirror":10,"mirror_hub":7,"hub":3,"bonnet":1,"UD-port":8,"LR-port":9},
{"mirror":9,"mirror_hub":8,"hub":3,"bonnet":2,"UD-port":8,"LR-port":9},
{"mirror":8,"mirror_hub":9,"hub":3,"bonnet":2,"UD-port":2,"LR-port":3},
{"mirror":5,"mirror_hub":10,"hub":3,"bonnet":1,"UD-port":0,"LR-port":1},
{"mirror":4,"mirror_hub":11,"hub":3,"bonnet":1,"UD-port":2,"LR-port":3},
{"mirror":3,"mirror_hub":12,"hub":3,"bonnet":1,"UD-port":4,"LR-port":5},
{"mirror":2,"mirror_hub":13,"hub":3,"bonnet":2,"UD-port":6,"LR-port":7},
{"mirror":1,"mirror_hub":14,"hub":3,"bonnet":2,"UD-port":0,"LR-port":1}
],

"hub4":[
{"mirror":46,"mirror_hub":0,"hub":4,"bonnet":0,"UD-port":0,"LR-port":1},
{"mirror":47,"mirror_hub":1,"hub":4,"bonnet":0,"UD-port":2,"LR-port":3},
{"mirror":36,"mirror_hub":2,"hub":4,"bonnet":0,"UD-port":6,"LR-port":7},
{"mirror":48,"mirror_hub":3,"hub":4,"bonnet":0,"UD-port":4,"LR-port":5},
{"mirror":37,"mirror_hub":4,"hub":4,"bonnet":0,"UD-port":8,"LR-port":9},
{"mirror":27,"mirror_hub":5,"hub":4,"bonnet":2,"UD-port":4,"LR-port":5},
{"mirror":49,"mirror_hub":6,"hub":4,"bonnet":1,"UD-port":6,"LR-port":7},
{"mirror":38,"mirror_hub":7,"hub":4,"bonnet":1,"UD-port":8,"LR-port":9},
{"mirror":28,"mirror_hub":8,"hub":4,"bonnet":2,"UD-port":8,"LR-port":9},
{"mirror":19,"mirror_hub":9,"hub":4,"bonnet":2,"UD-port":2,"LR-port":3},
{"mirror":50,"mirror_hub":10,"hub":4,"bonnet":1,"UD-port":0,"LR-port":1},
{"mirror":39,"mirror_hub":11,"hub":4,"bonnet":1,"UD-port":2,"LR-port":3},
{"mirror":29,"mirror_hub":12,"hub":4,"bonnet":1,"UD-port":4,"LR-port":5},
{"mirror":20,"mirror_hub":13,"hub":4,"bonnet":2,"UD-port":6,"LR-port":7},
{"mirror":12,"mirror_hub":14,"hub":4,"bonnet":2,"UD-port":0,"LR-port":1}
],

"hub5":[
{"mirror":56,"mirror_hub":0,"hub":5,"bonnet":0,"UD-port":0,"LR-port":1},
{"mirror":66,"mirror_hub":1,"hub":5,"bonnet":0,"UD-port":2,"LR-port":3},
{"mirror":57,"mirror_hub":2,"hub":5,"bonnet":0,"UD-port":6,"LR-port":7},
{"mirror":75,"mirror_hub":3,"hub":5,"bonnet":0,"UD-port":4,"LR-port":5},
{"mirror":67,"mirror_hub":4,"hub":5,"bonnet":0,"UD-port":8,"LR-port":9},
{"mirror":58,"mirror_hub":5,"hub":5,"bonnet":2,"UD-port":4,"LR-port":5},
{"mirror":83,"mirror_hub":6,"hub":5,"bonnet":1,"UD-port":6,"LR-port":7},
{"mirror":76,"mirror_hub":7,"hub":5,"bonnet":1,"UD-port":8,"LR-port":9},
{"mirror":68,"mirror_hub":8,"hub":5,"bonnet":2,"UD-port":8,"LR-port":9},
{"mirror":59,"mirror_hub":9,"hub":5,"bonnet":2,"UD-port":2,"LR-port":3},
{"mirror":90,"mirror_hub":10,"hub":5,"bonnet":1,"UD-port":0,"LR-port":1},
{"mirror":84,"mirror_hub":11,"hub":5,"bonnet":1,"UD-port":2,"LR-port":3},
{"mirror":77,"mirror_hub":12,"hub":5,"bonnet":1,"UD-port":4,"LR-port":5},
{"mirror":69,"mirror_hub":13,"hub":5,"bonnet":2,"UD-port":6,"LR-port":7},
{"mirror":60,"mirror_hub":14,"hub":5,"bonnet":2,"UD-port":0,"LR-port":1}
],

"hub6":[
{"mirror":55,"mirror_hub":0,"hub":6,"bonnet":0,"UD-port":0,"LR-port":1},
{"mirror":64,"mirror_hub":1,"hub":6,"bonnet":0,"UD-port":2,"LR-port":3},
{"mirror":65,"mirror_hub":2,"hub":6,"bonnet":0,"UD-port":6,"LR-port":7},
{"mirror":72,"mirror_hub":3,"hub":6,"bonnet":0,"UD-port":4,"LR-port":5},
{"mirror":73,"mirror_hub":4,"hub":6,"bonnet":0,"UD-port":8,"LR-port":9},
{"mirror":74,"mirror_hub":5,"hub":6,"bonnet":2,"UD-port":4,"LR-port":5},
{"mirror":79,"mirror_hub":6,"hub":6,"bonnet":1,"UD-port":6,"LR-port":7},
{"mirror":80,"mirror_hub":7,"hub":6,"bonnet":1,"UD-port":8,"LR-port":9},
{"mirror":81,"mirror_hub":8,"hub":6,"bonnet":2,"UD-port":8,"LR-port":9},
{"mirror":82,"mirror_hub":9,"hub":6,"bonnet":2,"UD-port":2,"LR-port":3},
{"mirror":85,"mirror_hub":10,"hub":6,"bonnet":1,"UD-port":0,"LR-port":1},
{"mirror":86,"mirror_hub":11,"hub":6,"bonnet":1,"UD-port":2,"LR-port":3},
{"mirror":87,"mirror_hub":12,"hub":6,"bonnet":1,"UD-port":4,"LR-port":5},
{"mirror":88,"mirror_hub":13,"hub":6,"bonnet":2,"UD-port":6,"LR-port":7},
{"mirror":89,"mirror_hub":14,"hub":6,"bonnet":2,"UD-port":0,"LR-port":1}
]

}  #end of mirror_hub mappings



mirrormappings=[
{"mirror":0,"mirror_hub":10,"hub":2,"bonnet":1,"UD-port":0,"LR-port":1},
{"mirror":1,"mirror_hub":14,"hub":3,"bonnet":2,"UD-port":0,"LR-port":1},
{"mirror":2,"mirror_hub":13,"hub":3,"bonnet":2,"UD-port":6,"LR-port":7},
{"mirror":3,"mirror_hub":12,"hub":3,"bonnet":1,"UD-port":4,"LR-port":5},
{"mirror":4,"mirror_hub":11,"hub":3,"bonnet":1,"UD-port":2,"LR-port":3},
{"mirror":5,"mirror_hub":10,"hub":3,"bonnet":1,"UD-port":0,"LR-port":1},
{"mirror":6,"mirror_hub":11,"hub":2,"bonnet":1,"UD-port":2,"LR-port":3},
{"mirror":7,"mirror_hub":6,"hub":2,"bonnet":1,"UD-port":6,"LR-port":7},
{"mirror":8,"mirror_hub":9,"hub":3,"bonnet":2,"UD-port":2,"LR-port":3},
{"mirror":9,"mirror_hub":8,"hub":3,"bonnet":2,"UD-port":8,"LR-port":9},
{"mirror":10,"mirror_hub":7,"hub":3,"bonnet":1,"UD-port":8,"LR-port":9},
{"mirror":11,"mirror_hub":6,"hub":3,"bonnet":1,"UD-port":6,"LR-port":7},
{"mirror":12,"mirror_hub":14,"hub":4,"bonnet":2,"UD-port":0,"LR-port":1},
{"mirror":13,"mirror_hub":12,"hub":2,"bonnet":1,"UD-port":4,"LR-port":5},
{"mirror":14,"mirror_hub":7,"hub":2,"bonnet":1,"UD-port":8,"LR-port":9},
{"mirror":15,"mirror_hub":3,"hub":2,"bonnet":0,"UD-port":4,"LR-port":5},
{"mirror":16,"mirror_hub":5,"hub":3,"bonnet":2,"UD-port":4,"LR-port":5},
{"mirror":17,"mirror_hub":4,"hub":3,"bonnet":0,"UD-port":8,"LR-port":9},
{"mirror":18,"mirror_hub":3,"hub":3,"bonnet":0,"UD-port":4,"LR-port":5},
{"mirror":19,"mirror_hub":9,"hub":4,"bonnet":2,"UD-port":2,"LR-port":3},
{"mirror":20,"mirror_hub":13,"hub":4,"bonnet":2,"UD-port":6,"LR-port":7},
{"mirror":21,"mirror_hub":13,"hub":2,"bonnet":2,"UD-port":6,"LR-port":7},
{"mirror":22,"mirror_hub":8,"hub":2,"bonnet":2,"UD-port":8,"LR-port":9},
{"mirror":23,"mirror_hub":4,"hub":2,"bonnet":0,"UD-port":8,"LR-port":9},
{"mirror":24,"mirror_hub":1,"hub":2,"bonnet":0,"UD-port":2,"LR-port":3},
{"mirror":25,"mirror_hub":2,"hub":3,"bonnet":0,"UD-port":6,"LR-port":7},
{"mirror":26,"mirror_hub":1,"hub":3,"bonnet":0,"UD-port":2,"LR-port":3},
{"mirror":27,"mirror_hub":5,"hub":4,"bonnet":2,"UD-port":4,"LR-port":5},
{"mirror":28,"mirror_hub":8,"hub":4,"bonnet":2,"UD-port":8,"LR-port":9},
{"mirror":29,"mirror_hub":12,"hub":4,"bonnet":1,"UD-port":4,"LR-port":5},
{"mirror":30,"mirror_hub":14,"hub":2,"bonnet":2,"UD-port":0,"LR-port":1},
{"mirror":31,"mirror_hub":9,"hub":2,"bonnet":2,"UD-port":2,"LR-port":3},
{"mirror":32,"mirror_hub":5,"hub":2,"bonnet":2,"UD-port":4,"LR-port":5},
{"mirror":33,"mirror_hub":2,"hub":2,"bonnet":0,"UD-port":6,"LR-port":7},
{"mirror":34,"mirror_hub":0,"hub":2,"bonnet":0,"UD-port":0,"LR-port":1},
{"mirror":35,"mirror_hub":0,"hub":3,"bonnet":0,"UD-port":0,"LR-port":1},
{"mirror":36,"mirror_hub":2,"hub":4,"bonnet":0,"UD-port":6,"LR-port":7},
{"mirror":37,"mirror_hub":4,"hub":4,"bonnet":0,"UD-port":8,"LR-port":9},
{"mirror":38,"mirror_hub":7,"hub":4,"bonnet":1,"UD-port":8,"LR-port":9},
{"mirror":39,"mirror_hub":11,"hub":4,"bonnet":1,"UD-port":2,"LR-port":3},
{"mirror":40,"mirror_hub":10,"hub":1,"bonnet":1,"UD-port":0,"LR-port":1},
{"mirror":41,"mirror_hub":6,"hub":1,"bonnet":1,"UD-port":6,"LR-port":7},
{"mirror":42,"mirror_hub":3,"hub":1,"bonnet":0,"UD-port":4,"LR-port":5},
{"mirror":43,"mirror_hub":1,"hub":1,"bonnet":0,"UD-port":2,"LR-port":3},
{"mirror":44,"mirror_hub":0,"hub":1,"bonnet":0,"UD-port":0,"LR-port":1},
{"mirror":45,"mirror_hub":15,"hub":2,"bonnet":0,"UD-port":10,"LR-port":11},
{"mirror":46,"mirror_hub":0,"hub":4,"bonnet":0,"UD-port":0,"LR-port":1},
{"mirror":47,"mirror_hub":1,"hub":4,"bonnet":0,"UD-port":2,"LR-port":3},
{"mirror":48,"mirror_hub":3,"hub":4,"bonnet":0,"UD-port":4,"LR-port":5},
{"mirror":49,"mirror_hub":6,"hub":4,"bonnet":1,"UD-port":6,"LR-port":7},
{"mirror":50,"mirror_hub":10,"hub":4,"bonnet":1,"UD-port":0,"LR-port":1},
{"mirror":51,"mirror_hub":11,"hub":1,"bonnet":1,"UD-port":2,"LR-port":3},
{"mirror":52,"mirror_hub":7,"hub":1,"bonnet":1,"UD-port":8,"LR-port":9},
{"mirror":53,"mirror_hub":4,"hub":1,"bonnet":0,"UD-port":8,"LR-port":9},
{"mirror":54,"mirror_hub":2,"hub":1,"bonnet":0,"UD-port":6,"LR-port":7},
{"mirror":55,"mirror_hub":0,"hub":6,"bonnet":0,"UD-port":0,"LR-port":1},
{"mirror":56,"mirror_hub":0,"hub":5,"bonnet":0,"UD-port":0,"LR-port":1},
{"mirror":57,"mirror_hub":2,"hub":5,"bonnet":0,"UD-port":6,"LR-port":7},
{"mirror":58,"mirror_hub":5,"hub":5,"bonnet":2,"UD-port":4,"LR-port":5},
{"mirror":59,"mirror_hub":9,"hub":5,"bonnet":2,"UD-port":2,"LR-port":3},
{"mirror":60,"mirror_hub":14,"hub":5,"bonnet":2,"UD-port":0,"LR-port":1},
{"mirror":61,"mirror_hub":12,"hub":1,"bonnet":1,"UD-port":4,"LR-port":5},
{"mirror":62,"mirror_hub":8,"hub":1,"bonnet":2,"UD-port":8,"LR-port":9},
{"mirror":63,"mirror_hub":5,"hub":1,"bonnet":2,"UD-port":4,"LR-port":5},
{"mirror":64,"mirror_hub":1,"hub":6,"bonnet":0,"UD-port":2,"LR-port":3},
{"mirror":65,"mirror_hub":2,"hub":6,"bonnet":0,"UD-port":6,"LR-port":7},
{"mirror":66,"mirror_hub":1,"hub":5,"bonnet":0,"UD-port":2,"LR-port":3},
{"mirror":67,"mirror_hub":4,"hub":5,"bonnet":0,"UD-port":8,"LR-port":9},
{"mirror":68,"mirror_hub":8,"hub":5,"bonnet":2,"UD-port":8,"LR-port":9},
{"mirror":69,"mirror_hub":13,"hub":5,"bonnet":2,"UD-port":6,"LR-port":7},
{"mirror":70,"mirror_hub":13,"hub":1,"bonnet":2,"UD-port":6,"LR-port":7},
{"mirror":71,"mirror_hub":9,"hub":1,"bonnet":2,"UD-port":2,"LR-port":3},
{"mirror":72,"mirror_hub":3,"hub":6,"bonnet":0,"UD-port":4,"LR-port":5},
{"mirror":73,"mirror_hub":4,"hub":6,"bonnet":0,"UD-port":8,"LR-port":9},
{"mirror":74,"mirror_hub":5,"hub":6,"bonnet":2,"UD-port":4,"LR-port":5},
{"mirror":75,"mirror_hub":3,"hub":5,"bonnet":0,"UD-port":4,"LR-port":5},
{"mirror":76,"mirror_hub":7,"hub":5,"bonnet":1,"UD-port":8,"LR-port":9},
{"mirror":77,"mirror_hub":12,"hub":5,"bonnet":1,"UD-port":4,"LR-port":5},
{"mirror":78,"mirror_hub":14,"hub":1,"bonnet":2,"UD-port":0,"LR-port":1},
{"mirror":79,"mirror_hub":6,"hub":6,"bonnet":1,"UD-port":6,"LR-port":7},
{"mirror":80,"mirror_hub":7,"hub":6,"bonnet":1,"UD-port":8,"LR-port":9},
{"mirror":81,"mirror_hub":8,"hub":6,"bonnet":2,"UD-port":8,"LR-port":9},
{"mirror":82,"mirror_hub":9,"hub":6,"bonnet":2,"UD-port":2,"LR-port":3},
{"mirror":83,"mirror_hub":6,"hub":5,"bonnet":1,"UD-port":6,"LR-port":7},
{"mirror":84,"mirror_hub":11,"hub":5,"bonnet":1,"UD-port":2,"LR-port":3},
{"mirror":85,"mirror_hub":10,"hub":6,"bonnet":1,"UD-port":0,"LR-port":1},
{"mirror":86,"mirror_hub":11,"hub":6,"bonnet":1,"UD-port":2,"LR-port":3},
{"mirror":87,"mirror_hub":12,"hub":6,"bonnet":1,"UD-port":4,"LR-port":5},
{"mirror":88,"mirror_hub":13,"hub":6,"bonnet":2,"UD-port":6,"LR-port":7},
{"mirror":89,"mirror_hub":14,"hub":6,"bonnet":2,"UD-port":0,"LR-port":1},
{"mirror":90,"mirror_hub":10,"hub":5,"bonnet":1,"UD-port":0,"LR-port":1}

]#end of mirror mappings


def getMirrorAddresses(mirror):
    if mirror<0 or mirror>=91:
        raise Exception('error', 'mirrormap.py invalid mirror ID:'+str(mirror))
    return (mirrormappings[mirror])

def getMirrorHubAddresses(hub, mirror_hub):
    if type(hub) is int: 
        hub = 'hub' + str(hub)    
    elif type(hub) is str: 
        if len(hub) == 1:
            hub = 'hub' + hub;
        else:
            pass
    
    return (hubmappings[hub][mirror_hub])
    
def getMirrorHubAddress(mirror):
    if mirror<0 or mirror>=91:
        raise Exception('error', 'mirrormap.py invalid mirror ID:'+str(mirror))
    return (mirrormappings[mirror]['mirror_hub'])
    
def getMirrorAddress(hub, mirror_hub):    
    if type(hub) is int: 
        hub = 'hub' + str(hub)    
    elif type(hub) is str: 
        if len(hub) == 1:
            hub = 'hub' + hub;
        else:
            pass
        
    return (hubmappings[hub][mirror_hub]['mirror'])
     
def getHubNumber(mirror):
    if mirror<0 or mirror>=91:
        raise Exception('error', 'mirrormap.py invalid mirror ID:'+str(mirror))
    return (mirrormappings[mirror]['hub'])
   

