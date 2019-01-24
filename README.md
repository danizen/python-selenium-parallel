# python-selenium-parallel
Some work to get Python tests written in selenium to run in parallel in both nosetests and pytest

## Assumptions

* Firefox is installed on your local computer
* A compatible version of the https://github.com/mozilla/geckodriver is also installed and in the path.

## Installation

* Clone this repository to your local computer
* Install the dependent packages, preferably in a virtual environment:

        pip install -r requirements.txt

## Usage

To run with one process, enter: 

    pytest 
    
To run with mulitple processes, enter:

    pytest -n 4
    
In this second case, you will see multiple browser windows be created.

## Key Considerations

A key consideration is how the Selenium webdriver is shared. The Webdriver API is not threadsafe, but as long as your parallelized tests each use their own webdriver, than they may be parallelized.

Another consideration is assuring that the webdriver connection is appropriately terminated. If you are doing a parallel test with a remote selenium grid, then your test can cause grid resources to be unavailable, e.g. to appear to leak, if your test doesn't clean-up carefully.

## License

MIT License

## Contributions

This is just a proof of concept, but if you have some ideas about the two Key Considerations, please submit a pull request to update this README.
