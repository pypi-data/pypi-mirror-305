import spec2flux


def main():
    # Spectrum details (adjust me with each star)
    spectrum_dir = 'spectra/epsInd_sw_coadd_v2_20241024.ecsv'
    rest_dir = 'DEM_goodlinelist.csv'
    airglow_dir = 'airglow.csv'
    observation = 'sci' # SCI only
    telescope = 'hst' # HST only
    instrument = 'stis' # STIS or COS only
    grating = 'e140l' # L or M grating only
    star_name = '20241024'
    min_wavelength = 1160

    # Spectrum adjustments
    apply_smoothing = False # True if want to apply gaussian smoothing
    line_fit_model = 'Voigt' # 'Voigt' or 'Gaussian' fit

    # User adjustable parameters
    fresh_start = True # True if first time running, or have already ran for a star and want to see final plot

    # Check inputs
    spec2flux.InputCheck(spectrum_dir, rest_dir, airglow_dir, observation, telescope, instrument, grating, star_name, 
               min_wavelength, apply_smoothing, line_fit_model, fresh_start)

    # Load spectrum data and emission lines
    spectrum = spec2flux.SpectrumData(spectrum_dir, rest_dir, airglow_dir, observation, telescope, instrument, grating, star_name, 
                            min_wavelength, apply_smoothing)
    emission_lines = spec2flux.EmissionLines(spectrum)

    # Calculate flux
    flux_calc = spec2flux.FluxCalculator(spectrum, emission_lines, fresh_start, line_fit_model)

    # Show final plot
    spectrum.final_spectrum_plot(emission_lines, flux_calc)


if __name__ == '__main__':
    main()

    print('All done!')