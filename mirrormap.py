# The MIRROR MAP
# 2019 by StrejcekBob
# This file contains the Mirror map that enables us to retrieve the hub, bonnet and the i2cports for a given mirror.
# Mirrormapping serves sofware & people that wish to operate mirrors based on their logical ID.

# funtions exposed:

# getMirrorAddress(mirror)
# returns a complete record for a mirror  : e.g. {"mirror":0,"hub":2,"bonnet":1,"UD-port":0,"LR-port":1}
# Sample code:
# import mirrormap as mm
# address=mm.getMirrorAddress(1)
# print(address['bonnet'])

# getMirroHub(mirror)      -returns the hub ID the mirror belongs to: e.g. 2
# Sample code:
# import mirrormap as mm
# print(mm.getMirroHub(2))
# would return 3

  



mirrormappings=[
{"mirror":0,"hub":2,"bonnet":1,"UD-port":0,"LR-port":1},
{"mirror":1,"hub":3,"bonnet":2,"UD-port":0,"LR-port":1},
{"mirror":2,"hub":3,"bonnet":2,"UD-port":6,"LR-port":7},
{"mirror":3,"hub":3,"bonnet":1,"UD-port":4,"LR-port":5},
{"mirror":4,"hub":3,"bonnet":1,"UD-port":2,"LR-port":3},
{"mirror":5,"hub":3,"bonnet":1,"UD-port":0,"LR-port":1},

{"mirror":6,"hub":2,"bonnet":1,"UD-port":2,"LR-port":3},
{"mirror":7,"hub":2,"bonnet":1,"UD-port":6,"LR-port":7},
{"mirror":8,"hub":3,"bonnet":2,"UD-port":2,"LR-port":3},
{"mirror":9,"hub":3,"bonnet":2,"UD-port":8,"LR-port":9},
{"mirror":10,"hub":3,"bonnet":1,"UD-port":8,"LR-port":9},
{"mirror":11,"hub":3,"bonnet":1,"UD-port":6,"LR-port":7},
{"mirror":12,"hub":4,"bonnet":2,"UD-port":0,"LR-port":0},

{"mirror":13,"hub":2,"bonnet":1,"UD-port":4,"LR-port":5},
{"mirror":14,"hub":2,"bonnet":1,"UD-port":8,"LR-port":9},
{"mirror":15,"hub":2,"bonnet":0,"UD-port":4,"LR-port":5},
{"mirror":16,"hub":3,"bonnet":2,"UD-port":4,"LR-port":5},
{"mirror":17,"hub":3,"bonnet":0,"UD-port":8,"LR-port":9},
{"mirror":18,"hub":3,"bonnet":0,"UD-port":4,"LR-port":5},
{"mirror":19,"hub":4,"bonnet":2,"UD-port":2,"LR-port":3},
{"mirror":20,"hub":4,"bonnet":2,"UD-port":6,"LR-port":7},

{"mirror":21,"hub":2,"bonnet":2,"UD-port":6,"LR-port":7},
{"mirror":22,"hub":2,"bonnet":2,"UD-port":8,"LR-port":9},
{"mirror":23,"hub":2,"bonnet":0,"UD-port":8,"LR-port":9},
{"mirror":24,"hub":2,"bonnet":0,"UD-port":2,"LR-port":3},
{"mirror":25,"hub":3,"bonnet":0,"UD-port":6,"LR-port":7},
{"mirror":26,"hub":3,"bonnet":0,"UD-port":2,"LR-port":3},
{"mirror":27,"hub":4,"bonnet":2,"UD-port":4,"LR-port":5},
{"mirror":28,"hub":4,"bonnet":2,"UD-port":8,"LR-port":9},
{"mirror":29,"hub":4,"bonnet":1,"UD-port":4,"LR-port":5},

{"mirror":30,"hub":2,"bonnet":2,"UD-port":0,"LR-port":1},
{"mirror":31,"hub":2,"bonnet":2,"UD-port":2,"LR-port":3},
{"mirror":32,"hub":2,"bonnet":2,"UD-port":4,"LR-port":5},
{"mirror":33,"hub":2,"bonnet":0,"UD-port":6,"LR-port":7},
{"mirror":34,"hub":2,"bonnet":0,"UD-port":0,"LR-port":1},
{"mirror":35,"hub":3,"bonnet":0,"UD-port":0,"LR-port":1},
{"mirror":36,"hub":4,"bonnet":0,"UD-port":6,"LR-port":7},
{"mirror":37,"hub":4,"bonnet":0,"UD-port":8,"LR-port":9},
{"mirror":38,"hub":4,"bonnet":1,"UD-port":8,"LR-port":9},
{"mirror":39,"hub":4,"bonnet":1,"UD-port":2,"LR-port":3},

{"mirror":40,"hub":1,"bonnet":1,"UD-port":0,"LR-port":1},
{"mirror":41,"hub":1,"bonnet":1,"UD-port":6,"LR-port":7},
{"mirror":42,"hub":1,"bonnet":0,"UD-port":4,"LR-port":5},
{"mirror":43,"hub":1,"bonnet":0,"UD-port":2,"LR-port":3},
{"mirror":44,"hub":1,"bonnet":0,"UD-port":0,"LR-port":1},
{"mirror":45,"hub":1,"bonnet":0,"UD-port":10,"LR-port":11},
{"mirror":46,"hub":4,"bonnet":0,"UD-port":0,"LR-port":1},
{"mirror":47,"hub":4,"bonnet":0,"UD-port":2,"LR-port":3},
{"mirror":48,"hub":4,"bonnet":0,"UD-port":4,"LR-port":5},
{"mirror":49,"hub":4,"bonnet":1,"UD-port":6,"LR-port":7},
{"mirror":50,"hub":4,"bonnet":1,"UD-port":0,"LR-port":1},

{"mirror":51,"hub":1,"bonnet":1,"UD-port":2,"LR-port":3},
{"mirror":52,"hub":1,"bonnet":1,"UD-port":8,"LR-port":9},
{"mirror":53,"hub":1,"bonnet":0,"UD-port":8,"LR-port":9},
{"mirror":54,"hub":1,"bonnet":0,"UD-port":6,"LR-port":7},
{"mirror":55,"hub":6,"bonnet":0,"UD-port":0,"LR-port":1},
{"mirror":56,"hub":5,"bonnet":0,"UD-port":0,"LR-port":1},
{"mirror":57,"hub":5,"bonnet":0,"UD-port":6,"LR-port":7},
{"mirror":58,"hub":5,"bonnet":2,"UD-port":4,"LR-port":5},
{"mirror":59,"hub":5,"bonnet":2,"UD-port":2,"LR-port":3},
{"mirror":60,"hub":5,"bonnet":2,"UD-port":0,"LR-port":1},


{"mirror":61,"hub":1,"bonnet":1,"UD-port":4,"LR-port":5},
{"mirror":62,"hub":1,"bonnet":2,"UD-port":8,"LR-port":9},
{"mirror":63,"hub":1,"bonnet":2,"UD-port":4,"LR-port":5},
{"mirror":64,"hub":6,"bonnet":0,"UD-port":2,"LR-port":3},
{"mirror":65,"hub":6,"bonnet":0,"UD-port":6,"LR-port":7},
{"mirror":66,"hub":5,"bonnet":0,"UD-port":2,"LR-port":3},
{"mirror":67,"hub":5,"bonnet":0,"UD-port":8,"LR-port":9},
{"mirror":68,"hub":5,"bonnet":2,"UD-port":8,"LR-port":9},
{"mirror":69,"hub":5,"bonnet":2,"UD-port":6,"LR-port":7},

{"mirror":70,"hub":1,"bonnet":2,"UD-port":6,"LR-port":7},
{"mirror":71,"hub":1,"bonnet":2,"UD-port":2,"LR-port":3},
{"mirror":72,"hub":6,"bonnet":0,"UD-port":4,"LR-port":5},
{"mirror":73,"hub":6,"bonnet":0,"UD-port":8,"LR-port":9},
{"mirror":74,"hub":6,"bonnet":2,"UD-port":4,"LR-port":5},
{"mirror":75,"hub":5,"bonnet":0,"UD-port":4,"LR-port":5},
{"mirror":76,"hub":5,"bonnet":1,"UD-port":8,"LR-port":9},
{"mirror":77,"hub":5,"bonnet":1,"UD-port":4,"LR-port":5},

{"mirror":78,"hub":1,"bonnet":2,"UD-port":0,"LR-port":1},
{"mirror":79,"hub":6,"bonnet":1,"UD-port":6,"LR-port":7},
{"mirror":80,"hub":6,"bonnet":1,"UD-port":8,"LR-port":9},
{"mirror":81,"hub":6,"bonnet":2,"UD-port":8,"LR-port":9},
{"mirror":82,"hub":6,"bonnet":2,"UD-port":2,"LR-port":3},
{"mirror":83,"hub":5,"bonnet":1,"UD-port":6,"LR-port":7},
{"mirror":84,"hub":5,"bonnet":1,"UD-port":2,"LR-port":3},

{"mirror":85,"hub":6,"bonnet":1,"UD-port":0,"LR-port":1},
{"mirror":86,"hub":6,"bonnet":1,"UD-port":2,"LR-port":3},
{"mirror":87,"hub":6,"bonnet":1,"UD-port":4,"LR-port":5},
{"mirror":88,"hub":6,"bonnet":2,"UD-port":6,"LR-port":7},
{"mirror":89,"hub":6,"bonnet":2,"UD-port":0,"LR-port":1},
{"mirror":90,"hub":5,"bonnet":1,"UD-port":0,"LR-port":1}

]#end of mirror mappings


def getMirrorAddress(mirror):
    if mirror<0 or mirror>90:
        raise Exception('mirrormap', 'invalid mirror ID:'+str(mirror))
    return (mirrormappings[mirror])
    
  
def getMirroHub(mirror):
    if mirror<0 or mirror>90:
        raise Exception('mirrormap', 'invalid mirror ID:'+str(mirror))
    return (mirrormappings[mirror]['hub'])


   

