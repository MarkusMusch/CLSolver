class Flux:

    def __init__(self, exact_flux: callable, numerical_flux: callable) -> None:
        self.exact_flux = exact_flux
        self.numerical_flux = numerical_flux
