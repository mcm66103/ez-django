$('<div class="mt-3 alert alert-warning d-flex" role="alert"><p class="mb-0 pb-0"><b>Are you ready to grow?</b> Start developing your digital strategy <a href="{% url 'Digital Strategy' %}">right here!</a><p></div>')
.insertAfter( $("#content-container")
.children("p:nth-child(8)"));


$('<img src="/media/{{ blog.featured_image.file }}" class="w-100 mb-2">')
.insertAfter( $("#content-container")
.children("p:nth-child(2)"));
