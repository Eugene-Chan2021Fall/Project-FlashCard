#def posts():
    '''
    This is a route that handles POST request from the user menu study timer.

    Returns
    -------
    Study session time.
    '''
    jsonobj = request.get_json()
    milisec = int(jsonobj["time"])
    hour_tracker = HoursTracked.query.get(current_user.get_id())
    hour_tracker.time += milisec
    db.session.commit()

    return '200'
