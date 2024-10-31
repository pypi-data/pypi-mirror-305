class MCAColObjectv1():
    def __init__(self):
        self.version = 1
        self.psetop_model = None
        self.psetop_model_key = None
        self.psetop_model_params = None
        self.psetop_model_params_key = None
        self.output_space_generator = None
        self.output_space_generator_key = None
        self.monitoring_data = None
        self.priority = None
        self.input_pset_models = dict() # key is index in input list
        self.input_pset_model_params = dict() # key is index in input list
        self.input_pset_model_monitoring = dict() # key is index in input list
        self.psetop_attributes_add = {}
        self.psetop_attributes_remove = []