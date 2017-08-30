'''
A translation function for contour.
'''

ELEVATOR_LINE_MAJOR = 500
ELEVATOR_LINE_MEDIUM = 50

def filterTags(attrs):
    if not attrs:
        return
    tags = {}

    if 'ele' in attrs:
        elevator = int(float(attrs['ele']))
        tags['ele'] = str(elevator)
        tags['contour'] = 'elevation'
        if elevator % ELEVATOR_LINE_MAJOR == 0:
            tags['contour_ext'] = 'elevation_major'
        elif elevator % ELEVATOR_LINE_MEDIUM == 0:
            tags['contour_ext'] = 'elevation_medium'
        else:
            tags['contour_ext'] = 'elevation_minor'

    #print 'filterTags()--------------'
    #print tags

    return tags