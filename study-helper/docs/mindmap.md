#def mindap_pdf():
    '''
    This is the route to make mindmap.

    Returns
    -------
    Renders the mindmap.html template.
    '''
    g = nx.Graph()
    # flashcards = Flashcardset.query.filter_by(author_id = current_user.get_id()).get(1)
    # g.add_nodes_from(flashcards)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(1, 4)
    g.add_edge(1, 5)

    nx.draw(g, with_labels = True)
    plt.savefig("plot.png")

    return render_template("mindmap.html")
