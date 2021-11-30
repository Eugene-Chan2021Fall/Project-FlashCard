#def stats():
    '''
    This is the home route endpoint.

    Returns
    -------
    Renders the home.html template.
    '''
    hours_tracked = HoursTracked.query.get(current_user.get_id())

    #Calculate milisec to hours
    time = hours_tracked.time
    time = round(time/1000)
    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600

    #Golden stars
    golden_stars = ""
    num_of_stars = 0
    for n in range(hour):
        golden_stars +=" X "
        num_of_stars += 1

    return render_template("user/stats.html", hours_tracked = hours_tracked, golden_stars = golden_stars, num = num_of_stars)
