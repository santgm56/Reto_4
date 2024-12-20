import math

class Point:
    """
    Entidad geometrica abstracta que representa una ubicación en un espacio.
    """

    # Este método inicializa los valores de x y y del punto a los valores 
    # pasados como parámetros.
    def __init__(self, x: float=0, y: float=0):
        self.__x = x
        self.__y = y

    # Setters and Getters de los atributos de Point
    
    """
    @property define un método que se comporta como un atributo de solo 
    lectura. Le agrega la funcionalidad de un getter.
    """
    @property
    def x(self):
        return self.__x
    
    """
    @x.setter define un método que se comporta como un atributo de solo 
    lectura escritura. Le agrega la funcionalidad de un setter.
    """
    @x.setter
    def x(self, value_x: float):
        self.__x = value_x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value__y: float):
        self.__y = value__y
        
    # Este método calcula la distancia entre dos puntos    
    def compute_distance(self, point: "Point")-> float:
        distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2 ) ** (0.5)
        return distance
    
    def __str__(self):
        return f"({self.x}, {self.y})"

class Line:  
    """
    Representa una línea en un espacio bidimensional. La línea es 
    definida por dos puntos: x, y; que hereda de la clase Point.
    """
    def __init__(self, start, end, n: int = 2):
        # Verifica que los puntos sean instancias de la clase Point
        if not isinstance(start, Point) or not isinstance(end, Point):
            raise ValueError("Los puntos deben ser instancias de la clase Point") 
            
        # Atributos de clase Point
        self.__start = start
        self.__end = end
        self.__length: float = self.compute_length()

    # Setters and Getters of attributes class Points
    @property
    def start(self):
        return self.__start
        
    @start.setter
    def start(self, point_start: Point):
        if not isinstance(point_start, Point):
            raise ValueError("""El punto de inicio debe ser una instancia 
                            de la clase Point""")
        self.__start = point_start
        self.__length = self.compute_length()

    @property
    def end(self):
        return self.__end
        
    @end.setter
    def end(self, point_end: Point):
        if not isinstance(point_end, Point):
            raise ValueError("""El punto de fin debe ser una instancia 
                            de la clase Point""")
        self.__end = point_end
        self.__length = self.compute_length()

    # Método que hereda de la clase Point y calcula la distancia 
    # entre los dos puntos
    def compute_length(self) -> float:
        return self.__start.compute_distance(self.__end)

    @property
    def length(self):
        return self.__length
    
    def __str__(self):
        return f"({self.start}) -> ({self.end})"

class Shape:
    """
    Esta clase representa una figura en un espacio bidimensional o
    tridimensional. La figura puede ser un triángulo o un rectángulo.
    Específicamente se definen las siguientes figuras:
    Triángulo: 
    - Equilátero: todos sus lados son iguales.
    - Isósceles: dos o tres lados son iguales.
    - Escaleno: todos sus lados son diferentes.
    - Tetraedro Trirrectángulo: tetraedro donde los tres ángulos de las 
    caras que convergen en un vértice son ángulos rectos
    Rectángulo:
    - Cuadrado: todos sus lados son iguales.
    """

    def vertices(self) -> list[Point]:
        """
        Devuelve los vértices de la figura.
        """
        raise NotImplementedError("Este método debe ser redefinido en las clases hijas.")

    def edges(self) -> list[Line]:
        """
        Devuelve las aristas de la figura.
        """
        raise NotImplementedError("Este método debe ser redefinido en las clases hijas.")

    def inner_angles(self) -> list[float]:
        """
        Devuelve los ángulos internos de la figura.
        """
        raise NotImplementedError("Este método debe ser redefinido en las clases hijas.")

    # Este método determina si una figura es regular
    def is_regular(self) -> bool:
        """
        Determina si una figura es regular.
        Para aprovechar el polimorfismo, este método debe ser
        implementado por las clases que heredan de Shape.
        """
        ...
    
    def compute_area(self) -> float:
        raise NotImplementedError("""Este método debe ser redefinido en 
                                las clases hijas.""")

    def compute_perimeter(self) -> float:
        raise NotImplementedError("""Este método debe ser redefinido en 
                                las clases hijas.""")

    def compute_inner_angles(self):
        raise NotImplementedError("""Este método debe ser redefinido en 
                                las clases hijas.""")
    
    def __str__(self):
        raise NotImplementedError("""Este método debe ser redefinido en 
                                las clases hijas.""")
    
class Rectangle(Shape):
    """
    Representa un rectángulo en un espacio bidimensional. 
    El rectángulo puede ser definido de tres maneras:
    1. Dando la esquina inferior izquierda y el ancho y alto.
    2. Dando el centro y el ancho y alto.
    3. Dando dos esquinas opuestas.
    """

    # Atributos de clase
    def __init__(self, *args):
        """
        Se inicializa el rectángulo con una de las siguientes configuraciones:
        - (bottom_left, width, height)
        - (center, width, height)
        - (bottom_left, top_right)
        """
        # Método 1: Esquina inferior izquierda + ancho y alto
        if len(args) == 3 and isinstance(args[0], Point):  
            bottom_left, width, height = args
            self.bottom_left = bottom_left
            self.width = width
            self.height = height
            self.center = Point(
                bottom_left.x + width / 2,
                bottom_left.y + height / 2,
            )
        # Método 2: Centro + ancho y alto
        elif len(args) == 3 and isinstance(args[0], Point) and isinstance(args[1], int):  
            center, width, height = args
            self.center = center
            self.width = width
            self.height = height
            self.bottom_left = Point(
                center.x - width / 2,
                center.y - height / 2,
            )
        elif len(args) == 2:  # Método 3: Dos esquinas opuestas
            bottom_left, top_right = args
            self.bottom_left = bottom_left
            self.width = top_right.x - bottom_left.x
            self.height = top_right.y - bottom_left.y
            self.center = Point(
                bottom_left.x + self.width / 2,
                bottom_left.y + self.height / 2,
            )
        else:
            raise ValueError("""Número de argumentos inválido para 
                            inicializar un rectángulo.""")

    def vertices(self):
        """Calcula los vértices del rectángulo."""
        return [
            self.bottom_left,
            Point(self.bottom_left.x + self.width, self.bottom_left.y),
            Point(self.bottom_left.x + self.width, self.bottom_left.y + self.height),
            Point(self.bottom_left.x, self.bottom_left.y + self.height),
        ]
    
    def edges(self):
        """Devuelve las líneas que forman los lados del rectángulo."""
        v = self.vertices()
        return [
            Line(v[0], v[1]),
            Line(v[1], v[2]),
            Line(v[2], v[3]),
            Line(v[3], v[0]),
        ]
    
    def inner_angles(self) -> list[float]:
        """Imprime los ángulos internos del rectángulo."""
        return self.compute_inner_angles()
    
    def is_regular(self) -> bool:
        """Determina si el rectángulo es regular."""
        return self.width == self.height
    
    def compute_perimeter(self) -> float:
        """Calcula el perímetro del rectángulo."""
        return 2 * (self.width + self.height)
    
    def compute_area(self) -> float:
        """Calcula el área del rectángulo."""
        return self.width * self.height

    def compute_inner_angles(self):
        """Devuelve los ángulos internos en radianes."""
        # Cada ángulo es 90 grados = π/2 radianes
        return [round(math.pi / 2, 4)] * 4 
    
    def __str__(self):
        # Generar información con cálculos
        vertices_str = ", ".join([f"({v.x}, {v.y})" for v in self.vertices()])
        edges_str = ", ".join([f"({e.start.x}, {e.start.y}) -> ({e.end.x}, {e.end.y})" for e in self.edges()])
        
        return (
            f"Este Rectángulo tiene las siguientes especificaciones:\n"
            f"- Esquina inferior izquierda: ({self.bottom_left.x}, {self.bottom_left.y})\n"
            f"- Dimensiones: Ancho = {self.width}, Alto = {self.height}\n"
            f"- Área: {self.compute_area()}\n"
            f"- Perímetro: {self.compute_perimeter()}\n"
            f"- Ángulos internos: {self.inner_angles()}\n"
            f"- Es regular: {'Sí' if self.is_regular() else 'No'}\n"
            f"- Vértices: {vertices_str}\n"
            f"- Lados (aristas): {edges_str}"
        )

class Square(Rectangle):
    """
    Clase que representa un cuadrado, un caso especial de un rectángulo donde 
    el ancho y la altura son iguales.
    """

    def __init__(self, bottom_left: Point, side_lenght: float):
        """
        Se inicializa el cuadrado con la esquina inferior izquierda 
        y el lado
        """
        super().__init__(bottom_left, side_lenght, side_lenght)
    
    def compute_area(self):
        return self.width ** 2
    
    def __str__(self):
        """Se reutiliza la lógica del dunder method __str__ de Rectangle 
        pero ajustar el encabezado"""
        rect_str = super().__str__()
        return rect_str.replace("Rectángulo", "Cuadrado")
    
class Triangle(Shape):
    """
    Representa un triángulo en un espacio bidimensional. 
    """
    def __init__(self, v1: Point, v2: Point, v3: Point):
        self.__v1 = v1
        self.__v2 = v2
        self.__v3 = v3

        if not self.is_valid_triangle():
            print("Los puntos no forman un triángulo válido")
        
    def is_valid_triangle(self):
        # Calcular las longitudes de los lados
        d1 = Line(self.__v1, self.__v2).compute_length()
        d2 = Line(self.__v2, self.__v3).compute_length()
        d3 = Line(self.__v3, self.__v1).compute_length()

        # Comprobación de la regla básica para formar un triángulo
        return (d1 + d2 > d3) and (d2 + d3 > d1) and (d1 + d3 > d2)

    @property
    def v1(self) -> Point:
        return self.__v1
    
    @v1.setter
    def v1(self, point: Point):
        self.__v1 = point

    @property
    def v2(self) -> Point:
        return self.__v2
    
    @v2.setter
    def v2(self, point: Point):
        self.__v2= point

    @property
    def v3(self) -> Point:
        return self.__v3
    
    @v3.setter
    def v3(self, point: Point):
        self.__v3 = point

    def vertices(self):
        """Calcula los vértices del triángulo."""
        return [self.__v1, self.__v2, self.__v3]

    @property
    def edges(self) -> list[Line]:
        """Calcula los lados del rectángulo."""
        v = self.vertices()
        return [
            Line(v[0], v[1]),
            Line(v[1], v[2]),
            Line(v[2], v[0]),
        ]
    
    def inner_angles(self):
        """Imprime los ángulos internos del triángulo."""
        return self.compute_inner_angles()

    def is_regular(self):
        """Determina si el triángulo es regular."""
        return all([line.compute_length() == self.edges[0].compute_length() for line in self.edges])
    
    def compute_perimeter(self):
        """Calcula el perímetro del triángulo."""
        return sum([line.compute_length() for line in self.edges])

    def compute_area(self):
        """Calcula el área del triángulo."""
        # Herón's formula
        a = self.edges[0].compute_length()
        b = self.edges[1].compute_length()
        c = self.edges[2].compute_length()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    def compute_inner_angles(self):
        """
        Calcula los ángulos internos utilizando la ley del coseno.
        Devuelve los ángulos en radianes.
        """
        a = self.edges[0].compute_length()
        b = self.edges[1].compute_length()
        c = self.edges[2].compute_length()

        # Ley del coseno para hallar los ángulos
        angle_A = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
        angle_B = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
        angle_C = math.acos((a**2 + b**2 - c**2) / (2 * a * b))

        return [round(angle, 6) for angle in [angle_A, angle_B, angle_C]]
    
    def __str__(self):
        vertices_str = ", ".join([f"({v.x}, {v.y})" for v in self.vertices()])
        edges_str = ", ".join([f"({e.start.x}, {e.start.y}) -> ({e.end.x}, {e.end.y})" for e in self.edges])

        return (
            f"Este triángulo tiene las siguientes especificaciones:\n"
            f"- Vértices: {vertices_str}\n"
            f"- Lados (aristas): {edges_str}\n"
            f"- Área: {self.compute_area()}\n"
            f"- Perímetro: {self.compute_perimeter()}\n"
            f"- Ángulos internos: {self.inner_angles()}\n"
            f"- Es regular: {'Sí' if self.is_regular() else 'No'}"
    )

class Isosceles(Triangle):
    """Clase para el triángulo isósceles."""
    def __init__(self, v1: Point, v2: Point, v3: Point):
        super().__init__(v1, v2, v3)
    
    def is_isosceles(self):
        """Determina si el triángulo es isósceles."""
        edges = [edge.compute_length() for edge in self.edges]
        return edges[0] == edges[1] or edges[1] == edges[2] or edges[2] == edges[0]
    
    def __str__(self):
        base_str = super().__str__()
        if self.is_isosceles():
            base_str = base_str.replace(
                "Este triángulo tiene:",
                "Este triángulo isósceles tiene:"
            )
            return f"{base_str} - Es un triángulo isósceles."
        else:
            return f"{base_str} - No es un triángulo isósceles."

class Equilateral(Triangle):
    """Clase para el triángulo equilátero."""
    def __init__(self, v1: Point, v2: Point, v3: Point):
        super().__init__(v1, v2, v3)

    def is_equilateral(self):
        """Determina si el triángulo es equilátero comparando la longitud de todos sus lados."""
        edge_lengths = [edge.compute_length() for edge in self.edges]
        return math.isclose(edge_lengths[0], edge_lengths[1], rel_tol=1e-9) and \
            math.isclose(edge_lengths[1], edge_lengths[2], rel_tol=1e-9) and \
            math.isclose(edge_lengths[0], edge_lengths[2], rel_tol=1e-9)


    """Sobrescribe el cálculo de área para evitar cálculos si no 
    es equilatero."""
    def inner_angles(self):
        if self.is_equilateral():
            return super().inner_angles()
        else:
            # Evita realizar cálculos para un triángulo que no es isósceles
            return [0, 0, 0]

    def compute_perimeter(self):
        if self.is_equilateral():
            return super().compute_perimeter()
        else:
            #Evita realizar cálculos para un triángulo que no es isósceles
            return 0
    
    def compute_area(self):
        if self.is_equilateral():
            return super().compute_area()
        else:
            # Evita realizar cálculos para un triángulo que no es isósceles
            return 0  

    def __str__(self):
        base_str = super().__str__() 
        # Verifica si es isósceles y ajusta la cadena de salida
        if self.is_equilateral():
            base_str = base_str.replace("Este triángulo tiene:", 
                                        "Este triángulo equilatero tiene:")
            return f"{base_str} - Es un triángulo equilatero."
        else:
            return f"{base_str} - No es un triángulo equilatero."

class Scalene(Triangle):
    """Clase para el triángulo escaleno."""
    def __init__(self, v1: Point, v2: Point, v3: Point):
        super().__init__(v1, v2, v3)

    def is_scalene(self):
        """Determina si el triángulo es escaleno."""
        edges = [edge.compute_length() for edge in self.edges]
        return len(set(edges)) == 3 
    
    """Sobrescribe el cálculo de perímetro para evitar cálculos si 
        no es escaleno."""
    def inner_angles(self):
        if self.is_scalene():
            return super().inner_angles()
        else:
            # Evita realizar cálculos para un triángulo que no es isósceles
            return [0, 0, 0]

    def compute_perimeter(self):
        if self.is_scalene():
            return super().compute_perimeter()
        else:
            #Evita realizar cálculos para un triángulo que no es isósceles
            return 0
    
    def compute_area(self):
        if self.is_scalene():
            return super().compute_area()
        else:
            # Evita realizar cálculos para un triángulo que no es isósceles
            return 0  

    def __str__(self):
        base_str = super().__str__() 
        # Verifica si es isósceles y ajusta la cadena de salida
        if self.is_scalene():
            base_str = base_str.replace("Este triángulo tiene:", 
                                        "Este triángulo escaleno tiene:")
            return f"{base_str} - Es un triángulo escaleno."
        else:
            return f"{base_str} - No es un triángulo escaleno."

class Trirectangle(Triangle):
    """
    Representa un triángulo rectángulo, que es un caso especial de triángulo.
    Hereda de la clase Triangle, utilizando la fórmula de Herón directamente.
    """

    def __init__(self, cateto_1: Point, cateto_2: Point):
        """
        Constructor para crear un triángulo rectángulo con dos catetos.
        Los puntos representan los catetos en un espacio bidimensional.
        """
        # Crear el tercer punto para formar el triángulo rectángulo
        hipotenusa_point = Point(cateto_1.x, cateto_2.y)
        
        # Llamar al constructor de la clase base con los 3 puntos
        super().__init__(cateto_1, cateto_2, hipotenusa_point)

    def is_right_triangle(self):
        """
        Verifica si el triángulo es un triángulo rectángulo.
        Ordena los lados para garantizar que el lado más largo sea la hipotenusa.
        """
        # Calcular longitudes de los lados
        lengths = [edge.compute_length() for edge in self.edges]
        lengths.sort()  # Ordena las longitudes de menor a mayor

        # Teorema de Pitágoras: cateto_1^2 + cateto_2^2 = hipotenusa^2
        a, b, c = lengths  # a y b son catetos, c es la hipotenusa
        return math.isclose(a**2 + b**2, c**2, rel_tol=1e-9)

    def __str__(self):
        base_str = super().__str__()
        if self.is_right_triangle():
            base_str = base_str.replace("Este triángulo tiene:",
                                        "Este triángulo rectángulo tiene:")
            return f"{base_str} - Es un triángulo rectángulo válido."
        else:
            return f"{base_str} - No es un triángulo rectángulo válido."

# Pruebas
print("Bienvenido a mi programa de geometría")

# Probar la clase Rectangle
v = Point(4, 3)

rect = Rectangle(v, 4, 6)
print(rect)

# Probar la clase Square
square = Square(v, 4)
print(square)

# Probar la clase Isosceles
v1 = Point(0, 0)
v2 = Point(4, 0)
v3 = Point(2, 4)
isosceles = Isosceles(v1, v2, v3)
print(isosceles)

# Probar la clase Equilateral
v1 = Point(0, 0)
v2 = Point(4, 0)
v3 = Point(2, 2 * math.sqrt(3))
equilateral = Equilateral(v1, v2, v3)
print(equilateral)

# Probar la clase Scalene
v1 = Point(0, 0)
v2 = Point(4, 0)
v3 = Point(0, 3)
scalene = Scalene(v1, v2, v3)
print(scalene)

# Probar la clase Trirectangle
v1 = Point(0, 0)
v2 = Point(4, 3)
tri_rect = Trirectangle(v1, v2)
print(tri_rect)