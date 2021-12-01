import numpy as np
from matplotlib import pyplot as plt 


def myFunc(x):
    """ 
    the function we want to integrate 

    """ 
    return np.multiply(np.exp(3 * x), np.sin(2 * x)) #hardcode the function you want

def rightHandRule(function, start, end, intervals):
    """
    Computes the Riemann Integral chosing the right endpoint (ending point) over (start,end)

    Parameters
    ----------
    function : ufunc
        the function we want to intergrate
    start : float
        the starting point of the integration
    end : float
        the ending point of the integration
    intervals : int
        the number of intervals we want to split the x axis for the integration

    Returns
    -------
    float
        the Riemann Integral

    """
    x = np.linspace(start, end, intervals + 1)
    values = function(x)
    intervalLength = (end - start) / intervals
    return intervalLength * sum(values[1::])

def leftHandRule(function, start, end, intervals):
    """
    Computes the Riemann Integral chosing the left endpoint (starting point) over (start,end) 

    Parameters
    ----------
    function: ufunc
        the function we want to intergrate
    start: float
        the starting point of the integration
    end: float
        the ending point of the integration
    intervals: int
        the number of intervals we want to split the x axis for the integration

    Returns
    -------
    float
        the Riemann Integral

    """
    x = np.linspace(start, end, intervals + 1)
    values = function(x)
    intervalLength = float((end - start) / intervals)
    return intervalLength * sum(values[0:intervals])

def trapezoidRule(function, start, end, intervals):
    """
    Computes the Trapezoid Integral over (start,end) 

    Parameters
    ----------
    function: ufunc
        the function we want to intergrate
    start: float
        the starting point of the integration
    end: float
        the ending point of the integration
    intervals: int
        the number of intervals we want to split the x axis for the integration
    
    Returns
    -------
    float
        the Trapezoid Integral

    """
    x = np.linspace(start, end, intervals + 1)
    values = function(x)
    intervalLength = float((end - start) / intervals)
    return (intervalLength / 2) * (values[0] + 2 * sum(values[1:intervals]) + values[intervals])

def simpsonsRule(function, start, end, intervals): 
    """
    Computes the Simpson's Integral over (start,end) 

     Parameters
    ----------
    function: ufunc
        the function we want to intergrate
    start: float
        the starting point of the integration
    end: float
        the ending point of the integration
    intervals: int
        the number of intervals we want to split the x axis for the integration

    Returns
    -------
    float
        the Simpson's Integral

    """
    x = np.linspace(start, end, 2*intervals + 1)
    values = function(x)
    intervalLength = float((end - start) / intervals)
    return (intervalLength / 6) * (values[0] + 2 * sum(values[:2 * intervals - 1:2]) + 4 * sum(values[1:2 * intervals:2]) + values[2 * intervals])   

def plotError(funcToIntegrate, ruleFunc, integralStart, integralEnd, trueValue, ruleString):
    """
    Plots log(h) in x axis and log(absolute error) in y axis

    Parameters
    ----------
    funcToIntegrate: ufunc
        the function we want to intergrate
    ruleFunc: function
        the function we use to integrate our funcToIntegrate
    integralStart: float
        the starting point of the integration
    integralEnd: float
        the ending point of the integration
    trueValue: float
        the theoretical known value of the integral
    ruleString: string
        the integration rule we use to integrate as String

    """
    x = list()
    y = list()
    for n in range(1, 400):             #basicly ranging the number of intervals from 1 to 200 and plotting the corresponding interval length (h)
        x.append(((integralEnd - integralStart) / n))
        y.append(np.absolute(trueValue - ruleFunc(funcToIntegrate, integralStart, integralEnd, int((integralEnd - integralStart) / x[n - 1]))))
    x = np.array(x)
    y = np.array(y)
    x = np.log(x)
    y = np.log(y)
    plt.plot(x,y) 
    plt.title("log-log " + ruleString)
    plt.xlabel("Interval length h") 
    plt.ylabel("Absolute error")
    #plt.savefig(ruleString + " LOG.png")
    plt.show()
    plt.close()


def riemannsMaxError(h):
    """
    Computes the maximum absolute error of the Riemann integration (right and left hand rule)
    for the function given in the assigmnent: e^3x*sin(2x), xΕ[0, π/4]
  
    Parameters
    ----------
    h: interval length

    Returns
    -------
    float
        the maximum absolute error of the integration

    """
    return (h/2) * (np.pi/4) * 3 * np.exp(3*np.pi/4)

def trapezoidMaxError(h):
    """
    Computes the maximum absolute error of the trapezoid rule integration 
    for the function given in the assigmnent: e^3x*sin(2x), xΕ[0, π/4]
  
    Parameters
    ----------
    h: interval length

    Returns
    -------
    float
        the maximum absolute error of the integration

    """
    return (np.power(h, 2) / 12) * (np.pi/4) * 56.94

def simpsonsMaxError(h):
    """
    Computes the maximum absolute error of the Simpson's rule integration 
    for the function given in the assigmnent: e^3x*sin(2x), xΕ[0, π/4]
  
    Parameters
    ----------
    h: interval length

    Returns
    -------
    float
        the maximum absolute error of the integration

    """
    return (np.power(h/2, 4) / 180) * (np.pi/4) * 126.84

def plotMaxError(ruleFunc, ruleMaxErrorFunc, ruleString):
    """
    Plots h in x axis and max absolute error in y axis,
    specificly for the function given in the assignment: e^3x*sin(2x), xΕ[0, π/4]

    Parameters
    ----------
    ruleMaxErrorFunc: func
        the max error function we use depending the integrationq rule we use
    ruleString: string
        the integration rule we use to integrate as String

    """
    x = list()
    y1 = list()
    y2 = list()
    for n in range(1, 200):   #basicly ranging the number of intervals from 1 to 200 and plotting the corresponding interval length (h)
        x.append((np.pi/4) / n)
        y1.append(ruleMaxErrorFunc(x[n - 1]))  #Max error
        y2.append(np.absolute((3 / 13) * np.exp(3 * np.pi /4) + 2 / 13 - ruleFunc(myFunc, 0, np.pi/4, int((np.pi/4) / x[n - 1]))))  #error of our computation
    x = np.array(x)
    y1 = np.array(y1)
    y2 = np.array(y2)
    plt.plot(x,y2)
    plt.plot(x,y1)
    plt.title(ruleString)
    plt.xlabel("Interval length h") 
    plt.legend(["Absolute error", "Max absolute error"])
    plt.savefig(ruleString + " MAX ERROR.png")
    
    plt.show()
    plt.close()


if __name__ == '__main__':
    myFunc = np.frompyfunc(myFunc, 1, 1) #transforming our function into ufunc

    plotError(myFunc, leftHandRule, 0, np.pi / 4, (3 / 13) * np.exp(3 * np.pi /4) + 2 / 13, "Left Hand Rule")
    plotError(myFunc, rightHandRule, 0, np.pi / 4, (3 / 13) * np.exp(3 * np.pi /4) + 2 / 13, "Right Hand Rule")
    plotError(myFunc, trapezoidRule, 0, np.pi / 4, (3 / 13) * np.exp(3 * np.pi /4) + 2 / 13, "Trapezoid Rule")
    plotError(myFunc, simpsonsRule, 0, np.pi / 4, (3 / 13) * np.exp(3 * np.pi /4) + 2 / 13, "Simpson's Rule")

    plotMaxError(leftHandRule, riemannsMaxError, "Left Hand Rule")
    plotMaxError(rightHandRule, riemannsMaxError, "Right Hand Rule")
    plotMaxError(trapezoidRule, trapezoidMaxError, "Trapezoid Rule")
    plotMaxError(simpsonsRule, simpsonsMaxError, "Simpson's Rule")

 
