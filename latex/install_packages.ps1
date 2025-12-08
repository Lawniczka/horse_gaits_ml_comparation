# ===================================================================
# LaTeX Package Installer for Your Thesis Project (Minimal TeX Live)
# ===================================================================

# List of required TeX Live packages
$packages = @(
    "dirtree",       # \usepackage{dirtree}
    "multirow",      # \usepackage{multirow}
    "calc",          # \usepackage{calc}
    "amsfonts",      # \usepackage{amsfonts}
    "psfrag",        # \usepackage{psfrag}
    "supertabular",  # \usepackage{supertabular}
    "array",         # \usepackage{array}
    "tabularx",      # \usepackage{tabularx}
    "hhline",        # \usepackage{hhline}
    "minted",        # \usepackage{minted}
    "url",           # \usepackage{url}
    "microtype",     # \usepackage{microtype}
    "booktabs",      # \usepackage{booktabs}
    "makecell",      # \usepackage{makecell}
    "rotating",      # \usepackage{rotating}
    "multicol",      # \usepackage{multicol}
    "cuted",         # \usepackage{cuted}
    "colortbl",      # \usepackage{colortbl}
    "adjustbox",     # \usepackage{adjustbox}
    "color",         # \usepackage{color}
    "xcolor",        # Required by color and highlighting packages
    "soul",          # \usepackage{soul}
    "subfigure",     # \usepackage{subfigure}
    "pdfpages",      # \usepackage{pdfpages}
    "pifont",        # \usepackage{pifont}
    "caption",       # \usepackage{caption}
    "cite",          # \usepackage{cite}
    "svg",           # \usepackage{svg}
    "tabto",         # \usepackage{tabto}
    "wrapfig",       # \usepackage{wrapfig}
    "fancyhdr",      # for \fancypagestyle
    "algorithm2e",   # if your thesis uses algorithms
    "ifoddpage",     # required by algorithm2e
    "footmisc",      # recommended to replace \usepackage{footnote}
    "xspace",        # for custom commands
    "babel-polish",  # Polish language support
    "hyperref",      # almost always needed
    "geometry"       # page formatting
)

# Install all packages
foreach ($pkg in $packages) {
    Write-Host "Installing $pkg ..."
    tlmgr install $pkg
}

Write-Host "All packages installation attempt completed."
