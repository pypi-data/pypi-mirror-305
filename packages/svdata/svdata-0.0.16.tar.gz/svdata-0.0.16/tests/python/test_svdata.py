from svdata import SvInstance, SvModule, SvPort, SvPortDirection, read_sv_file

ansi_module_a = read_sv_file("tests/systemverilog/ansi_module_a.sv").modules[0]
ansi_module_b = read_sv_file("tests/systemverilog/ansi_module_b.sv").modules[0]
ansi_module_c = read_sv_file("tests/systemverilog/ansi_module_c.sv").modules[0]


def test_module_name() -> None:
    assert ansi_module_a.identifier == "ansi_module_a"

    assert ansi_module_a.ports[0].identifier == "a"
    assert ansi_module_a.ports[0].direction == SvPortDirection.Input
    assert str(ansi_module_a.ports[0]) == "input tri logic a"

    assert ansi_module_a.ports[1].identifier == "b"
    assert ansi_module_a.ports[1].direction == SvPortDirection.Input
    assert ansi_module_a.ports[1].unpacked_dimensions[0].left_bound == "2"
    assert ansi_module_a.ports[1].unpacked_dimensions[0].right_bound == "0"
    assert ansi_module_a.ports[1].packed_dimensions[0].left_bound == "1"
    assert ansi_module_a.ports[1].packed_dimensions[0].right_bound == "0"
    assert str(ansi_module_a.ports[1]) == "input var logic [1:0] b[2:0]"

    assert ansi_module_a.variables[0].identifier == "c"

    assert ansi_module_a.variables[1].identifier == "d"
    assert str(ansi_module_a.variables[2]) == "logic [1:0] ponta[2:0];"


def test_inits() -> None:
    SvModule(identifier="bla", filepath="bla", ports=[], variables=[], instances=[])
    SvInstance("bla", "bla", [])
    SvPort("", SvPortDirection.Input, [], [])


def test_ansi_module_a_repr() -> None:
    with open("tests/systemverilog/ansi_module_a.sv", "r") as file:
        assert str(ansi_module_a) == file.read()

    with open("tests/systemverilog/ansi_module_b.sv", "r") as file:
        assert str(ansi_module_b) == file.read()

    with open("tests/systemverilog/ansi_module_c.sv", "r") as file:
        assert str(ansi_module_c) == file.read()


def test_add_connection() -> None:
    instance = SvInstance("bla", "bla", [])
    assert instance.connections == []
    instance.add_connection(["asd", "asd"])
    assert instance.connections == [["asd", "asd"]]
