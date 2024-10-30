#[cfg(test)]
mod tests {
    use svdata::{read_sv_file, sv_port_direction::SvPortDirection};

    #[test]
    fn test_read_sv_file_success() {
        let result = read_sv_file("tests/systemverilog/ansi_module_a.sv");
        assert!(result.is_ok());
        let sv_data = result.unwrap();

        assert_eq!(sv_data.modules.len(), 1);
        let module = &sv_data.modules[0];
        assert_eq!(module.identifier, "ansi_module_a");
        assert_eq!(module.ports.len(), 2);
        assert_eq!(module.ports[0].identifier, "a");
        assert_eq!(module.ports[0].direction, SvPortDirection::Input);
        assert_eq!(module.ports[1].identifier, "b");
        assert_eq!(module.ports[1].direction, SvPortDirection::Input);

        assert_eq!(module.variables.len(), 3);
        assert_eq!(module.variables[0].identifier, "c");
        assert_eq!(module.variables[1].identifier, "d");

        assert_eq!(module.instances.len(), 4);
        assert_eq!(module.instances[0].instance_identifier, "ansi_module_b_i");
        assert_eq!(module.instances[0].module_identifier, "ansi_module_b");
        assert_eq!(module.instances[0].connections.len(), 1);
        assert_eq!(module.instances[0].connections[0][0], "e");
        assert_eq!(module.instances[0].connections[0][1], "d");
    }

    #[test]
    fn test_read_sv_file_failure() {
        let result = read_sv_file("non_existent_file.sv");
        assert!(result.is_err());
    }

    #[test]
    fn test_sv_port_direction() {
        assert_eq!(SvPortDirection::Input.to_string(), "input");
        assert_eq!(SvPortDirection::Output.to_string(), "output");
        assert_eq!(SvPortDirection::Inout.to_string(), "inout");
    }

    #[test]
    fn test_wire_logic_variable() {
        let result = read_sv_file("tests/systemverilog/ansi_module_b.sv");
        assert!(result.is_ok());
        let sv_data = result.unwrap();
    }
}
