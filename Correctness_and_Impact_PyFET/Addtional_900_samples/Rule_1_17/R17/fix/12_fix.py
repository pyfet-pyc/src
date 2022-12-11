
def test_routes_endpoint_legacy(serve_instance):
    @serve.deployment
    class D1:
        pass

    @serve.deployment(route_prefix="/hello/world")
    class D2:
        pass

    D1.deploy()
    D2.deploy()

    routes = requests.get("http://localhost:8000/-/routes").json()

    assert len(routes) == 2, routes
    assert "/D1" in routes, routes
    assert routes["/D1"] == "D1", routes
    assert "/hello/world" in routes, routes
    assert routes["/hello/world"] == "D2", routes

    D1.delete()

    routes = requests.get("http://localhost:8000/-/routes").json()
    assert len(routes) == 1, routes
    assert "/hello/world" in routes, routes
    assert routes["/hello/world"] == "D2", routes

    D2.delete()
    routes = requests.get("http://localhost:8000/-/routes").json()
    assert len(routes) == 0, routes

    app = FastAPI()

    @serve.deployment(route_prefix="/hello")
    @serve.ingress(app)
    class D3:
        pass

    D3.deploy()

    routes = requests.get("http://localhost:8000/-/routes").json()
    assert len(routes) == 1, routes
    assert "/hello" in routes, routes
    assert routes["/hello"] == "D3", routes
