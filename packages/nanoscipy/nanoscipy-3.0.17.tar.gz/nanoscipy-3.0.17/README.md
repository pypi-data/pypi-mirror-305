# nanoscipy

nanoscipy has been made, to ease the data-handling, -processing, and - analysis. Additionally, it also provides a 
simple way to perform numerical calculations with units.
This package is being readily updated at the moment, so be sure to keep up, as new and useful additions and fixes are 
very likely to be included.

## Installation and updating
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install nanoscipy like below. 
Rerun this command to check for and install  updates .
```bash
pip install nanoscipy
```
For package updates, use:
```bash
pip install --upgrade nanoscipy
```
Note that if you're using anaconda, you might have to install the module from the anaconda terminal instead (or use 
conda rather than pip)

## Import
<details><summary>Click for details</summary>
<p>
Currently, the package consists of four distinct modules:
```bash
nanoscipy.functions
```
Contains most of the practical functions of nanoscipy. 

```bash
nanoscipy.modules
```
Contains all classes of nanoscipy.

```bash
nanoscipy.util
```
Contains all utility functions and lists used within nanoscipy. Different modules use functions from this module. 
Note that some of these functions may be of practical use, but many are simply throw-away functions to increase 
readability.

```bash
nanoscipy.mathpar
```
The module with the mathematical parser of nanoscipy. Specifically, this contains the practical function parser(), which
is the collective parser itself.

```bash
nanoscipy.unitpar
```
Contains a script that allows for computation with units. 
</p>
</details>

## Getting started with unit computations
<details><summary>Click for details</summary>
<p>
There are two main functions of concern here; `mathpar.parser()` and `unitpar.unit_parser()`, but the focus will be on 
the module `modules.NumAn` as this is what is meant to be the 'calculator'. This section will serve as an explanation of how 
it works and how it may be used for different purposes.
(Last updated: v3.0.8)

### 1) The NumAn object
When defining the NumAn object there are a few things to note. The `__init__()` function takes five different inputs, 
all of which are optional. The first is `cons` which is where initial constants can be defined so that they may be used 
in computations later on (by default no constants are defined), e.g.:
```python
import nanoscipy.modules as nsm
cal1 = nsm.NumAn('A=234 kg, lambda=53 nm')
```
Will have the constants `A` and `lambda` defined with the values `234 kg` and `53 nm` assigned to them, respectively.
Constants may also be defined via the attribute function `.add_cns()`, which works in much the same way, so that for
```python
import nanoscipy.modules as nsm
cal2 = nsm.NumAn()
cal2.add_cns('A=234 kg, lambda=53 nm')
```
the same constants are defined as for the `cal1` object. 
The add-constant attribute does, however, work slightly different, allowing for new constants to be defined with 
previously defined constants, so
```python
cal2.add_cns('A2=4*A')
```
would make it so that `A2=936 kg`. 
Constants may effectively have any desired name with a few exceptions: The constant must be a string, meaning that it 
cannot be converted to a float or int, so `B2=34` is allowed, but `22=34` is not. Be aware that constant-values are 
substituted before calculations are done, which means that if a constant `2H=4` is defined, and a calculation is done 
for a string `'32H'` the result is `'3*2H=3*4=12'`.

The second parameter is `unit_identifier`. This defines an identifier for which units can be told apart from defined 
constants by the different scripts. This can in principle be set to any symbol, but be smart about it. The default
value used for this purpose is `' '`, which is illustrated in the examples above. Another example is seen below for 
`unit_identifier='~'`
```python
import nanoscipy.modules as nsm
cal3 = nsm.NumAn(unit_identifier='~')
cal3.add_cns('A=234~kg, lambda=53~nm')
cal3.add_cns('A2=4*A')
```

The third parameter is `units`. This tells the script whether units should be used or not (explicitly). Effectively, 
this only affects natural constants used (see [More about constants](https://github.com/nicholas12392/nanoscipy#2-more-about-constants)). 
Therefore, the default setting is `units=True` meaning that the script will act as computations should be done with units. 
Setting this to `False` will have the script do calculations without units (effectively). It must although be emphasized that this __only__ affects natural constants
and so everything is still fine if no units are used initially, as long as no natural constants are used, unless it is 
by division or multiplication, in which case it is also fine.

The next parameter is `cprint`. This affects how the result from a computation is displayed (the console print), and affects all 
computations if not anything else is set specifically per computation (see [Calculations](https://github.com/nicholas12392/nanoscipy#3-calculations)). 
There are a few options here, but the main difference is between `'num'` and `'sym'`. If set to `'num'` the result will 
be displayed as the `mathpar.parser()` reads the expression, i.e. with only numbers and mathematical symbols. If set to `'sym'` the 
expression will be displayed with symbols/constants rather than numbers. A variance is `'symc'`, which displays the
constants used in the expression, along with the result. Subtypes are `'sym_ex'` and `'symc_ex'`, which will display
the main expression with explicit multiplication (if any implicit multiplication was used). If set to `None` or `False` 
no console print is done. Examples can be found in 
[Calculations](https://github.com/nicholas12392/nanoscipy#3-calculations). The default setting is `'symc_ex'`.

The last parameter is `sf` which sets the significant figures for the console print. It is important to note that it 
does not change the significant figures of the calculation itself nor the result. It __only__ changes the console print.
This parameter takes integer values, and can be set to `None` if no evaluation is desired. The default value is 4. Note 
that this feature works by using the `mpmath.workdps` function.

### 2) More about constants
There has already been presented examples of how constants may be defined, but there are a few additional features to 
note. A list of all the currently defined constants can be seen by calling the attribute function `.constants()`. Note
that if constants are defined with units, then they are _displayed_ with `' '` as the unit identifier, regardless of the 
value of `unit_identifier` in the `__init__()` call. When adding constants that have already been defined, the new 
constant value will overwrite the old, and a prompt will be printed in the console. E.g.: 
```python
cal1 = nsm.NumAn('A=234 kg, lambda=53 nm')
cal1.add_cns('A=34 g')
```
```
>>> Constant 'A = 234 kg' has been changed to '34 g'.
```
Constants may also be removed with the attribute function `.del_cns()`. Simply specify which constants should be removed 
in the call. E.g. from the example above: 
```python
cal1.constants()
```
```
>>> Currently defined constants:
>>> | lambda = 53 nm
>>> | A = 34 g
```
```python
cal1.del_cns('A, lambda')
cal1.constants()
```
```
>>> Currently defined constants:
```

Note here that `.del_cns()` can also be used with multiple arguments, rather than with a single string, e.g.: 
```python
cal1.del_cns('A', 'lambda')
cal1.constants()
```
```
>>> Currently defined constants:
```

Constants may also be defined from latest computed result by calling the attribute function `.add_res()` with the name 
of the constant, e.g. `.add_res('omega')` will add the latest result from computation as the constant `'omega'`.

Other than the constants that can be defined by the user, there are some pre-defined natural constants, which may be 
used in all calculations, in which they might be needed. These are constants such as the Boltzmann constant `_k`, the 
Planck constant `_h` or the speed of light in a vacuum `_c`. Note that all constants are denoted with an underscore.
A full list of the supported units can be seen by calling the attribute `.supported_physical_constants`. 
Depending on whether `units` is set to `True` or `False`, these natural constants will either have associated units or will 
simply be the natural constant value with SI units:

```python
test = nsm.NumAn(units=False)
print(test.supported_physical_constants)
```
```
>>> ('_hbar=1.0545718176461565e-34', ..., '_mp=1.67262192369e-27')
```
```python
test = nsm.NumAn(units=True)
print(test.supported_physical_constants)
```
```
>>> ('_hbar=(1.0545718176461565e-34 J Hz^-1)', ..., '_mp=(1.67262192369e-27 kg)')
```
### 3) Calculations
Calculations are performed via the `.calc()` attribute function. This effectively utilizes `unitpar.unit_parser()`, 
which utilizes `mathpar.parser()` to compute the numerical part of the expression. An example of basic usage is seen 
below: 
```python
import nanoscipy.modules as nsm
cal = nsm.NumAn()
cal.calc('3*5+2^2')
```
```
>>> Result: 3·5+2^2 = 19
19
```

There are a few things to note here. As seen, the support for mathematical operators is slightly different compared to 
normal python. Specifically, there is support for the operations; `+, -, *, /, ^, !` (currently, there is no support 
for the usual way of denoting a power as `**`). There is also a 'prettifier' built-in, which automatically changes 
constants and specific operations to be more in line with how it would look, when simply writing it out on a piece of 
paper. An example of this is with the use of constants; 

```python
cal.add_cns('omega=34 s^-1, d=4 m')
cal.calc('domega')
```
```
>>> Result: d·ω = 136 m s^-1
>>> | ω = 34 s^-1
>>> | d = 4 m
136
```

This also illustrates a feature regarding implicit multiplication, as this is also read properly by the script (which
is why caution must be made, when defining constants). Note also that the units will be in the displayed result from 
the console, but they are not a part of the returned output (to obtain the unit, the attribute `.__ans_unit__` can be
called). 
The result from the calculation can be directly added to the list of constants by calling the attribute function 
`.add_res()` in the call with a specified name:

```python
cal.add_res('v')
cal.constants()
```
```
>>> Currently defined constants:
>>> | omega = 34 s^-1
>>> | d = 4 m
>>> | v = 136 m s^-1
```
Note that a result may be directly added as a constant, by specifying the parameter `add_res` in the `.calc()` call: 
```python
cal.calc('domega', 'v', cprint=None)
cal.constants()
```
```
>>> Currently defined constants:
>>> | omega = 34 s^-1
>>> | d = 4 m
>>> | v = 136 m s^-1
```

This also shows use of the `cprint` (local) kwarg. As opposed to setting the console print option in the `__init__()` 
when defining the function as described in [The NumAn object](https://github.com/nicholas12392/nanoscipy#1-the-numan-object).
When set in `.calc()` it only changes the console print for that single calculation, and all others will follow the 
default set in `__init__()`:

```python
cal.calc('2d/omega', cprint='num')
```
```
>>> Result: 2·(4 m)/(34 s^-1) = 0.2353 m s
0.23529411764705882
```

```python
cal.calc('2domega')
```
```
>>> Result: 2·d·ω = 272 m s^-1
>>> | ω = 34 s^-1
>>> | d = 4 m
272
```

As seen in the former calculation, the significant figures in the console print differs from the output. This is due to 
described evaluation feature `sf` ([The NumAn object](https://github.com/nicholas12392/nanoscipy#1-the-numan-object)). This
parameter can also be set locally with a kwarg per calculation: 

```python
cal.add_cns('m=12.3432 g, a=834.2325 m s^-2')
cal.calc('ma')
```
```
>>> Result: m·a = 10.3 N
>>> | m = 12.34 g
>>> | a = 834.2 m
10.297098594
```

```python
cal.calc('ma', sf=6)
```
```
>>> Result: m·a = 10.2971 N
>>> | m = 12.3432 g
>>> | a = 834.233 m
10.297098594
```

As seen, the parameter also affects the displayed constants. Another example (also illustrating the use of natural 
constants): 

```python
cal.add_cns('T=293.15 K')
cal.calc('T_k')
```
```
>>> Result: T·kᴮ = 4.047e-21 J
>>> | T = 293.1 K
4.0473725435e-21
```

Another thing to note is that there is native support for many mathematical functions such as the trigonometric functions, 
the natural logarithm, etc. The full list of supported such functions (including the value of pi), can be found by calling
the attribute `.__exclusions__`. Some examples of use: 

```python
cal.calc('sin(deg(45))')
```
```
>>> Result: sin(deg(45)) = 0.8061
0.8060754911159176
```

```python
cal.add_cns('E=0.3 eV')
cal.calc('exp(E/_kT)')
```
```
>>> Result: exp(-E/(kᴮ·T)) = 6.958e-6 a.u.
>>> | T = 293.1 K
>>> | E = 0.3 eV
6.95757565703751e-06
```

```python
cal.calc('sin(2pi)')
```
```
>>> Result: sin(2·π) = 0
0
```
Note that the natural logarithm is denoted by `'ln()'`, whereas log10 is denoted as `'log()'`.

### 4) The units
A note must be made about the functionality of the units. In general, when computing the units, all given units
are converted into their respective SI components and then reduced. At last, if they correspond to a _directly_ derived unit
the resulting unit will be changed into that derived unit. It is, however, currently quite limited, what the script can 
recognize as a derived unit. Only the base units e.g. `N, K, J` and the inverse base units; `N^-1, K^-1, J^-1` can be 
found. If the unit result cannot be recognized as a derived unit, it is simply given as SI units.

There is currently support for the vast majority of the SI unit derivatives, excluding the candela derived units. There 
is also special support for some other units such as the atomic mass unit (amu or u), Angstrom (Å), atmosphere (atm), etc.
The full list of supported units, can be seen by calling the attribute `.supported_units`. 

There is also an important point to be made in regard to denotation of the units in an expression. The working principle
of the units is that they are essentially multiplicative factors, and so all units act like they are just that. With one
very significant exception. When writing units in fractions, if the unit in the denominator consists of multiple units, 
only the first of those will be read as being in the denominator. This is best illustrated with an example: 

```python
import nanoscipy.modules as nsm
test = nsm.NumAn()
test.calc('23 m/2 s')
```
```
>>> Result: 23 m/2 s = 11.5 m s^-1
11.5
```
```python
test.calc('23 m/2 s g')
```
```
>>> Result: 23 m/2 s g = 0.0115 m kg s^-1
0.0115
```

As seen in the latter, the expression `'23 m/2 s g'` is being read as `'(23* m/2* s)* g'` rather than `'23* m/(2* s* g)'`.
Due to this, it is __always__ recommended to write expressions with units in parentheses (this is automatically handled, 
when defining constants and using them in expressions, as shown above, so that a constant defined as `'A=4 kg'` will be 
used by the script as `'A=(4 kg)`), especially as this odd functionality may change in the future, but as of now, the way
to go is: 

```python
test.calc('23 m/(2 s g)')
```
```
>>> Result: 23 m/(2 s g) = 1.15e+4 m s^-1 kg^-1
11500
```

Note that there is currently no support for doing square-roots as `'sqrt(4 m^2)'`:
```python
test.calc('sqrt(4 m^2)')
```
```
>>> Result: sqrt(4 m^2) = 2 m^2
2
```

```python
test.calc('(4 m^2)^(1/2)')
```
```
>>> Result: (4 m^2)^(1/2) = 2 m
2
```


### 5) Tips and tricks
It may be convenient to reduce the amount of code needed to do computations, especially if the script is run in a console
environment rather than an IDE. This can be done by defining the attribute functions as short variables as follows:

```python
import nanoscipy.modules as nsm
cal = nsm.NumAn()
a = cal.add_cns
d = cal.del_cns
c = cal.calc
```

Then, when adding new constants simply run `a()`, when deleting constants, `d()` and when doing computations `c()`. E.g.: 

```python
a('theta=rad(74), gamma=3.412')
c('gammacos(theta)')
d('gamma')
cal.constants()
```
```
>>> Result: γ·cos(θ) = 0.9405
>>> | θ = 1.292
>>> | γ = 3.412
>>> Currently defined constants:
>>> | theta = 1.2915436464758034
```

### 6) Disclaimer
Note importantly that this guide may not be completely up-to-date with the newest version of nanoscipy, as it takes a lot
of time to re-write and keep an overview of what is in and what is missing. Therefore, I will always recommend to check 
out the [patch notes](https://github.com/nicholas12392/nanoscipy/releases). 
It is noted in the beginning of the guide, which version the guide is currently up-to-date with. 
</p>
</details>
