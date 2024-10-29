# SuperRad

SuperRad is an open-source python code for modelling ultralight boson clouds
that arise through black hole superradiance. It uses numerical
results in the relativistic regime combined with analytic estimates to describe
the dynamics and gravitational wave signals of ultralight scalar or vector clouds.

## Installation 

### From PyPI 

```shell
pip install superrad
```

### From source

```shell
git clone git@bitbucket.org:weast/superrad.git
cd superrad
pip install .
```

## Dependencies

* Required: [numpy](https://docs.scipy.org/doc/numpy/user/install.html), [scipy](https://www.scipy.org/install.html)

* Optional (for running examples): [matplotlib](https://matplotlib.org/stable/users/installing/index.html)

These can all be installed with pip or conda. The package has been tested in the following configurations:

Python 3.10.12: numpy 1.26.1, scipy 1.11.3

Python 3.6.9: numpy 1.19.5, scipy 1.5.4

## Contact

[Nils Siemonsen](https://www.nilssiemonsen.com)

[Taillte May](https://perimeterinstitute.ca/people/taillte-may)

[William East](https://www2.perimeterinstitute.ca/personal/weast/)

## License

SuperRad is licensed under the BSD 3-Clause License. See LICENSE for details.

## Citation

To acknowledge using this package, please cite the following references:

```
@article{Siemonsen:2022yyf,
    author = "Siemonsen, Nils and May, Taillte and East, William E.",
    title = "{Modeling the black hole superradiance gravitational waveform}",
    eprint = "2211.03845",
    archivePrefix = "arXiv",
    primaryClass = "gr-qc",
    doi = "10.1103/PhysRevD.107.104003",
    journal = "Phys. Rev. D",
    volume = "107",
    number = "10",
    pages = "104003",
    year = "2023"
}
@article{May:2024,
    author = "May, Taillte and East, William E. and Siemonsen, Nils",
    title = "{Self-gravity effects of ultralight boson clouds formed by black hole superradiance}",
    journal = "in prep.",
    year = "2024"
}
```

## Usage

For a given ultralight boson spin and cloud model (described below), one first creates an `UltralightBoson` object.  Here spin-1 is chosen, corresponding to a vector, but spin-0, i.e. a scalar, is supported as well. (Regarding massive spin-2 fields, see note at the end.) For some models, this requires reading in data files, etc., but only needs to be done once.

```python
>>> from superrad import ultralight_boson as ub
>>> bc = ub.UltralightBoson(spin=1, model="relativistic")
```

A waveform model can then be constructed corresponding to specific physical parameters of the system, in this case an initial black hole of 20.8 solar masses, dimensionless spin of 0.7, and an ultralight boson mass of 1.16e-12 electronvolts. 

```python
>>> wf = bc.make_waveform(20.8, 0.7, 1.16e-12, units="physical")
```

This can be used to determine various properties of the black hole-boson cloud system that arises through the superradiant instability. For example:

```python
>>> wf.cloud_growth_time() # Cloud growth time in seconds
6057.590376604236
>>> wf.mass_cloud(0) #Cloud mass at saturation in solar mass
0.37023402627248814
>>> wf.spin_bh_final() #Final black hole spin 
0.6216222486933041
```

It can also be used to calculate the resulting gravitational wave signal as a function of time.

```python
>>> import numpy as np
>>> sec_hour = 3600.0
>>> t = np.linspace(0,24*sec_hour, 256) #time
>>> thetaObs = np.pi/3 #Observing angle w.r.t. spin axis
>>> hp,hx,delta = wf.strain_amp(t, thetaObs, dObs=100) # Strain at d=100 Mpc
>>> fgw = wf.freq_gw(t)
```

Plotting this

```python
>>> from matplotlib import pyplot as plt
>>> fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
>>> ax1.plot(t/sec_hour, hp, label=r"$h_+$")
>>> ax1.plot(t/sec_hour, hx, label=r"$h_\times$")
>>> ax1.set_ylabel(r"$h$")
>>> ax1.legend(loc="best")
>>> ax2.plot(t/sec_hour, fgw)
>>> ax2.set_ylabel(r"$f_{\rm GW}$ (Hz)")
>>> ax2.set_xlabel(r"$t$ (hours)")
>>> plt.show()
```
produces (with a bit of formatting) the following:

![strain_freq_example plot](documentation/strain_freq_example.png)

More examples can be found in [examples/run_example.py](examples/run_example.py) in the source code.

## Contributing

We welcome contributions. If you find a bug or issue, please let us know through the [issue tracker](https://bitbucket.org/weast/superrad/issues?status=new&status=open). If you want to extend `superrad` substantially, feel free to reach out to us.

## Updates

Various updates and upgrades `superrad` has received:

v0.2.0:

* Added relativistic frequency shift calculations for m=1 modes and spins 0 and 1 [May, East, and Siemonsen][2], along with some additional data on orbits around black holes with boson clouds, as described below.
* Replaced default frequency shift calculation for higher m modes with the non-relativistic calculation in [Siemonsen, May, and East][1]


v0.1.1:

* Added massive spin-2 unstable mode frequencies and growth rates [[East and Siemonsen](https://arxiv.org/abs/2309.05096)] as detailed below.
* Update `superrad` to make compatible with more recent python, numpy, and scipy versions.

v0.1.0: 

* First `superad` version

## Documentation

Here we document the front-end functionality of `superrad`.

**1. UltralightBoson(spin=sp,model="relativistic")**

*Creates an UltralightBoson object with a specified CloudModel.*

Parameters:

* `sp` is the spin of the ultralight boson being considered. Can take the values 0 or 1, for scalar or vector bosons respectively.

* `model` can take values `"relativistic"` or `"non-relativistic"` depending on the regime of interest. 
The most accurate results are obtained with `"relativistic"` by interpolating over numerical data. 
The `"non-relativistic"` results are calculated analytically in the α << 1 limit  (where α is the dimensionless product of the boson mass and black hole mass) and can be used for comparison, for parameters not covered by `"relativistic"` (currently azimuthal numbers >2),
or for faster results when accuracy is not important. These two models are discussed further below.

Returns:

* Returns an object of the UltralightBoson class.

**1.1. UltralightBoson.make_waveform(self, Mbh, abh, mu, units="physical", evo_type="matched", nonrel_freq_shift=False)**

*Returns an object of the BosonCloudWaveform class.*

Parameters:

* `Mbh` is the initial black hole mass (before cloud growth).

* `abh` is the initial black hole dimensionless spin (before cloud growth), 0 < `abh` ≤ 1.

* `mu` is the ultralight boson mass.

* `units` specifies the units for input/output. Can take values `"physical"` or `"natural"`. Physical units are as follows: {mu : electronvolts, Mass : solar mass, time : seconds, frequency : Hz, Power : watts, Distance : Mpc}. Natural units assume G = c = hbar = 1. Note that, for natural units, the black hole mass should in units of the Planck mass in order for the cloud growth time (time for the cloud to grow from a single boson to saturation) to give a sensible result. If "+alpha" is appended to either "physical" or "natural," then units are the same as above, except the input `mu` is taken to be in units of (hbar c^3)/(G Mbh) , i.e. mu is set to the dimensionless "fine structure constant" alpha.

* `evo_type` can take values `evo_type="full"` or `evo_type="matched"`.  The "matched" evolution assumes that the boson cloud decays solely through gravitational radiation after reach its peak mass (by definition, t=0), and matches this on to a exponentially growing solution with constant growth rate before the peak mass is obtained (t<0). Hence, it is not very accurate around t=0, and in particular the derivative of the frequency will be discontinuous at this point. The "full" evolution option numerically integrates the ordinary differential equations describing the cloud mass and black hole mass and spin, and hence is more accurate for scenarios when the signal before the time when the cloud reaches saturation makes a non-negligible contribution. However, it is significantly more computationally expensive, and the numerical integration is not always robust. This option should currently be considered experimental. Details and a comparison of these methods can be found in the [main paper][1]. 

*If `nonrel_freq_shift` is set to `True`, than the non-relativistic calculation of the boson cloud self-gravity frequency is always used. This is included mainly for comparison purposes, and the default value of `False` will give the most accurate calculation the particular model has.

Returns:

* Object of the BosonCloudWaveform class.


**2. BosonCloudWaveform(mu, Mbh, abh, cloud_model, units="natural")**

*Calculates some derived quantities using the specified CloudModel and for a given black hole and boson field.*

Parameters:

* `Mbh` is the initial black hole mass (before cloud growth).

* `abh` is the initial black hole dimensionless spin (before cloud growth), 0 < `abh` ≤ 1.

* `mu` is the ultralight boson mass.

* `cloud_model` specifies the spin of the boson and whether to perform calculations using a relativistic or non-relativistic model. Within SuperRad,
`cloud_model` has options `NonrelScalar()`, `NonrelVector()`, `RelScalar()` and
`RelVector()`.

* `units` specifies the units for input/output and is the same as in UltralightBoson.make_waveform().

Returns:

* An object of the BosonCloudWaveform class.
 
**2.1. BosonCloudWaveform.efold_time()**

*Gives the e-folding time of the growth of the mass of the boson cloud during the instability phase, before the saturation of the superradiance condition.*

Parameters: None

Returns: 

* E-folding time of cloud mass, in units specified for the waveform.

**2.2. BosonCloudWaveform.cloud_growth_time()**

*Returns the time for cloud to grow from a single boson to saturation.*

Parameters: None

Returns: 

* Growth time in units specified for the waveform.

**2.3. BosonCloudWaveform.mass_cloud(t)**

*Returns the mass of the boson cloud as a function of time.*

Parameters:

* `t` is time where `t=0` corresponds to the time when the cloud mass is at its maximum.

Returns:

* Mass at time `t` in units specified for the waveform.

**2.4. BosonCloudWaveform.gw_time()**

*Gives the characteristic timescale of GW emission (Mcloud/P_{GW}) at saturation.*

Parameters: None

Returns:

* Gravitational wave emission timescale in units specified for the waveform.
 
**2.5. BosonCloudWaveform.power_gw(t)**

*Returns power (luminosity) of gravitational waves as a function of time.*

Parameters:

* `t` is time where `t=0` corresponds to the time when the cloud mass is at its maximum.

Returns:

* Gravitational wave power at time `t` in units specified for the waveform.
 
**2.6. BosonCloudWaveform.freq_gw(t)**

*Gives the frequency of the gravitational wave signal as a function of time.*

Parameters:

* `t` is time where `t=0` corresponds to the time when the cloud mass is at its maximum.

Returns:

* Frequency at time `t` in units specified for the waveform.

**2.7. BosonCloudWaveform.freqdot_gw(t)**

*Returns the time derivative of the frequency of the gravitational wave signal as a function of time.*

Parameters:

* `t` is time where `t=0` corresponds to the time when the cloud mass is at its maximum.

Returns:

* Frequency drift at time `t` in units specified for the waveform.

**2.8. BosonCloudWaveform.phase gw(t)**

*Return the gravitational wave phase as a function of time. Here we assume (take the approximation) that dω/dMcloud is a constant. By convention, the phase is zero at t = 0.*

Parameters:

* `t` is time where `t=0` corresponds to the time when the cloud mass is at its maximum.

Returns:

* Gravitational wave phase at time `t`.
 
**2.9. BosonCloudWaveform.strain_char(t, dObs=None)**

*Returns a characteristic strain value, defined to be:*

![h_0 := (10 P_{GW}(t)^(1/2) ) / (ω_{GW}dObs)](documentation/h0_pw.svg)

*In the non-relativistic limit (and for azimuthal num=1), we have that:*

![h_x = h_0 cos(θ) sin(φ(t)); h_+ = h_0 /2 (1 + cos^2(θ)) cos(φ(t)](documentation/hplus_cross.svg)

Parameters:

* `t` is time where `t=0` corresponds to the time when the cloud mass is at it's maximum.

* `dObs` is distance to source.

Returns:

* Gravitational wave strain h_0 at time `t`.
 
**2.10. BosonCloudWaveform.strain amp(t, thetaObs, dObs=None)**

*Returns the magnitude of the two polarizations of the strain (h_+, h_x ). This function also returns δ, where δ is the extra phase difference between polarizations. That is, the observed strain in terms
of the antenna-response functions of detector I is:*

![h_I = F^I_+(t) h_+(t) cos(φ(t)) + F^I_x h_x(t) sin(φ(t)+δ)](documentation/hI.svg)

*Implicitly, an alignment between the observer's and the cloud's azimuthal angle is assumed
at t=0, but arbitrary azimuthal viewing angles can be obtained trivially by rotation.* 

Parameters:

* `t` is time where `t=0` corresponds to the time when the cloud mass is at its maximum.

* `thetaObs` is the inclination angle in radians with respect to spin axis of the source.

* `dObs` is distance to the source.

Returns: 

* (h_+ , h_x , δ) at time `t`.
 
**2.11 BosonCloudWaveform.mass_bh_final()**

*Returns the black hole mass after the superradiant instability saturates.*

Parameters: None

Returns:

* Black hole mass at saturation. 
 
**2.12 BosonCloudWaveform.spin_bh_final()**

*The black hole dimensionless spin after the superradiant instability saturates.*

Parameters: None

Returns:

* Dimensionless spin of the black hole at saturation.
 
**2.13 BosonCloudWaveform.azimuthal_num()**

*Gives the azimuthal mode number of the boson cloud. The azimuthal number of the gravitational waves is twice this.
This is the azimuthal number of just the fastest growing mode.*

Parameters: None

Returns:

* Azimuthal number m.
 
**3. CloudModel**

*Abstract base class encompassing functions needed to compute ultralight boson cloud gravitational waves. All inputs are in natural units where the black hole mass Mbh = G = c = 1. In the `superrad` package, the implemented cloud models are: `RelScalar`, `RelVector`, `NonrelScalar`, and `NonrelVector`.*

**3.1. CloudModel.max_azi_num()**

*Finds the maximum azimuthal number for which the model is defined.*

Parameters: None

Returns:

* Azimuthal number m, above which the model will produce an error message.

**3.2. CloudModel.max_spin()**

*Finds the maximum spin for which the model is defined.*

Parameters: None

Returns:

* Dimensionless spin above which the model will produce an error message.
 
**3.3. CloudModel.omega_real(m, alpha, abh, Mcloud)**

*Returns the real frequency of the boson cloud’s oscillation.*

Parameters:

* `m` is the azimuthal mode number.

* `alpha` is the dimensionless product of the boson mass and the black hole mass.

* `abh` is the dimensionless spin of the black hole.

* `Mcloud` is the cloud mass as a fraction of the black hole mass.

Returns:

* Real frequency of cloud oscillation in natural units, where Mbh = 1.
 
**3.4. CloudModel.domegar_dmc(m, alpha, abh, Mcloud)**

*Returns the derivative of the real frequency of the boson cloud with respect to cloud mass.*

Parameters:

* `m` is the azimuthal mode number.

* `alpha` is the dimensionless product of the boson mass and the black hole mass.

* `abh` is the dimensionless spin of the black hole.

* `Mcloud` is the cloud mass as a fraction of the black hole mass.

Returns:

* Derivative of real frequency of cloud oscillation with respect to cloud mass, in natural units and where Mbh = 1.

**3.5. CloudModel.omega_imag(m, alpha, abh)**

*Returns the imaginary frequency of the boson cloud, i.e. the growth rate of the superradiant instability.*

Parameters:

* `m` is the azimuthal mode number.

* `alpha` is the dimensionless product of the boson mass and the black hole mass.

* `abh` is the dimensionless spin of the black hole.

Returns:

* Imaginary frequency in natural units and where Mbh = 1.
 
**3.6. CloudModel.power_gw(m, alpha, abh)**

*Returns the gravitational wave power, scaled to Mcloud = 1.*

Parameters:

* `m` is the azimuthal mode number.

* `alpha` is the dimensionless product of the boson mass and the black hole mass.

* `abh` is the dimensionless spin of the black hole.

Returns:

* Gravitational wave power in natural units and scaled to: P_{GW} Mcloud^2 / Mbh^2
 
**3.7. CloudModel.strain_sph_harm(m, alpha, abh)**

*Gives the strain for the leading −2-weighted spherical harmonic components. The number of components returned is implementation dependent.*

Parameters:

* `m` is the azimuthal mode number.

* `alpha` is the dimensionless product of the boson mass and the black hole mass.

* `abh` is the dimensionless spin of the black hole.

Returns:

* `numpy` array e^{i ω t}R h^{2 l m} (−2-weighted spherical harmonic components).
 
**4. RelScalar(CloudModel)** and **RelVector(CloudModel)**  

Implementations of `CloudModel` for scalar and vectors bosons, respectively. These are the cloud models used when the `model="relativistic"` option is chosen in `UltralightBoson()`. The calculations used for these are described in detail in the [main reference][1]. The 
the relativistic self-gravity frequency correction (for m=1) used in these models are described in the [second reference][2] (this can be turned off with the optional argument `nonrel_freq_shift=True`). 

*Warning: These models are not guaranteed to cover points in the parameter space where there is no superradiant instability. When called at such a point, functions will in general return Nan. These models are valid from `abh=0` to `abh=0.995`. Also, for the calculation of gravitational wave quantities, the cloud is implicitly assumed to be in the saturated state (in particular, the value of the 
black hole spin is ignored).*  

**5. NonRelScalar(CloudModel)** and **NonRelVector(CloudModel)**  

Implementations of `CloudModel` for scalar and vectors bosons. These are the cloud models used when the `model="non-relativistic"` option is chosen in `UltralightBoson()`. For the non-relativistic power calculation we use results from the literature -- for the scalar m = 1 case: Eq. (13) in [Brito et al](https://doi.org/10.1088/0264-9381/32/13/134001), for the scalar m > 1 case: Eq. (57) in [Yoshino et al.](https://doi.org/10.1093/ptep/ptu029), for vector boson m = 1 case: from [Siemonsen et al.](https://link.aps.org/doi/10.1103/PhysRevD.101.024019), and for the vector m > 1 case: from [Baryakhtar et al.](https://link.aps.org/doi/10.1103/PhysRevD.103.095019).

For the non-relativistic frequencies, the results from [Baumann et al.](https://ui.adsabs.harvard.edu/abs/2019JCAP...12..006B) are used, with the frequency shift due to self-gravity as described in our [accompanying paper][1]. 

**6. Redshift dependence**

SuperRad is configured to take the luminosity distance `dObs` as input argument. All input times are given in the source frame. However, since the superradiant growth timescales, gravitational wave emission timescales, and the associated gravitational wave frequency and frequency evolution as measured in the detector frame depend on the redshift, it might be of use to obtain the correctly redshifted results. For a given time in the detector frame `tdet`, the time of the source frame `tsrc` is redshifted by `tsrc=tdet/(1+z)` for a given redshift `z`. Using a relation between the luminosity distance `dObs` and the reshift `z`, here just called `D(z)`, the correctly redshifted quantities are obtained from `superrad` as follows:

```python
>>> sec_hour = 3600.0
>>> tdet = np.linspace(0,24*sec_hour, 256) #time in detector frame
>>> tsrc = tdet/(1+z) #time in source frame at redshift z
>>> thetaObs = np.pi/3 #Observing angle w.r.t. spin axis
>>> hp,hx,delta = wf.strain_amp(tsrc, thetaObs, dObs=D(z)) # Strain at luminosity distance D(z)
>>> fgw = wf.freq_gw(tsrc)/(1+z) #frequency in detector frame
```

Notice, `superrad` does not include such a relation `D(z)` between the luminosity distance `dObs` and redshift `z`; it must be calculated externally.

## Testing

The waveform model comes with a set of testing routines that check the internal consistency of `superrad`. All tests can be run with [test/run_test.py](test/run_test.py) in the source code. These tests mainly serve the purpose of ensuring functionality of the waveform model even after updating the source code (i.e., are useful for code development). However, the tests can also be utilized by the user to check that `superrad` works as intended.

## Massive spin-2 fields 

Massive spin-2 (tensor) fields can also be unstable in the presence of a black hole (even a non-spinning one), though the subsequent backreaction will depend on the particular nonlinear theory and is largely unknown. Spin-2 fields are not currently supported by SuperRad, though numerical data for the linear instability rates around black holes computed in [East and Siemonsen](https://arxiv.org/abs/2309.05096) can be found in [superrad/data/spin2_omega.dat](superrad/data/spin2_omega.dat) and can be plotted with [examples/plot_spin2_modes.py](examples/plot_spin2_modes.py).

## Orbit Calculations

The geometry around a black hole with a superradiance boson cloud deviate from that around an isolated black hole. We include data files wit numerical values for the equatorial light ring radius, ISCO radius, frequency, and redshift (for light emitted both in the same or opposite direction as the emitter orbiting at the ISCO) of black holes with m=1 complex scalar and vector boson clouds as described in [May, East, and Siemonsen][2]. The data can be read and interpolated using [superrad/geometry.py](superrad/geometry.py) and plotted with the final example in [examples/run_example.py](examples/run_example.py).  

## Additional notes

There is a typo in the expression for scalar `m=2` and `relativistic` growthrate in the [accompanying paper][1] (see end of Appendix C). For this scalar mode, q takes on integer values between zero and two only, and `-1.1948426572069112e11*alpha**12+2.609027546773062e12*alpha**13` are missing on the right hand side of eq. (15) in the [accompanying paper][1]. This typo was pointed out to us by [Dent et al.](https://arxiv.org/abs/2404.02956) The package `superrad` contained the correct expressions throughout.

[1]: <https://arxiv.org/abs/2211.03845>
[2]: <https://arxiv.org/search/?query=may+east+siemonsen&searchtype=author>
