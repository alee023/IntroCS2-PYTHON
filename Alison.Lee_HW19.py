# Alison Lee
# IntroCS2 pd8
# HW19 -- Slice, Dice, Replace
# 2016-3-22

# 1
def tablefyASCII ( ) :
    n = 65
    print "<!DOCTYPE html> \n <html> <table border = '1'> <tr> <td> Letter </td> <td> ASCII </td> </tr>"
    # prints HTML code for the first row 
    while n <= 90 :
    # A - Z is from 65 - 90
        print "<tr> <td> " + str( chr( n )) + " </td> <td> " + str( n ) + " </td> </tr>"
        n += 1
    n = 97
    while n <= 122 :
    # a - z is from 97 - 122
        print "<tr> <td> " + str( chr( n )) + " </td> <td> " + str( n ) + " </td> </tr>"
        n += 1
    print "</table> </html>"         

tablefyASCII ( )
# should result in :
# <!DOCTYPE html> 
# <html> <table border = '1'> <tr> <td> letter </td> <td> ASCII </td> </tr>
# <tr> <td> A</td> <td> 65</td> </tr>
# <tr> <td> B</td> <td> 66</td> </tr>
# <tr> <td> C</td> <td> 67</td> </tr>
# <tr> <td> D</td> <td> 68</td> </tr>
# <tr> <td> E</td> <td> 69</td> </tr>
# <tr> <td> F</td> <td> 70</td> </tr>
# <tr> <td> G</td> <td> 71</td> </tr>
# <tr> <td> H</td> <td> 72</td> </tr>
# <tr> <td> I</td> <td> 73</td> </tr>
# <tr> <td> J</td> <td> 74</td> </tr>
# <tr> <td> K</td> <td> 75</td> </tr>
# <tr> <td> L</td> <td> 76</td> </tr>
# <tr> <td> M</td> <td> 77</td> </tr>
# <tr> <td> N</td> <td> 78</td> </tr>
# <tr> <td> O</td> <td> 79</td> </tr>
# <tr> <td> P</td> <td> 80</td> </tr>
# <tr> <td> Q</td> <td> 81</td> </tr>
# <tr> <td> R</td> <td> 82</td> </tr>
# <tr> <td> S</td> <td> 83</td> </tr>
# <tr> <td> T</td> <td> 84</td> </tr>
# <tr> <td> U</td> <td> 85</td> </tr>
# <tr> <td> V</td> <td> 86</td> </tr>
# <tr> <td> W</td> <td> 87</td> </tr>
# <tr> <td> X</td> <td> 88</td> </tr>
# <tr> <td> Y</td> <td> 89</td> </tr>
# <tr> <td> Z</td> <td> 90</td> </tr>
# <tr> <td> a</td> <td> 97</td> </tr>
# <tr> <td> b</td> <td> 98</td> </tr>
# <tr> <td> c</td> <td> 99</td> </tr>
# <tr> <td> d</td> <td> 100</td> </tr>
# <tr> <td> e</td> <td> 101</td> </tr>
# <tr> <td> f</td> <td> 102</td> </tr>
# <tr> <td> g</td> <td> 103</td> </tr>
# <tr> <td> h</td> <td> 104</td> </tr>
# <tr> <td> i</td> <td> 105</td> </tr>
# <tr> <td> j</td> <td> 106</td> </tr>
# <tr> <td> k</td> <td> 107</td> </tr>
# <tr> <td> l</td> <td> 108</td> </tr>
# <tr> <td> m</td> <td> 109</td> </tr>
# <tr> <td> n</td> <td> 110</td> </tr>
# <tr> <td> o</td> <td> 111</td> </tr>
# <tr> <td> p</td> <td> 112</td> </tr>
# <tr> <td> q</td> <td> 113</td> </tr>
# <tr> <td> r</td> <td> 114</td> </tr>
# <tr> <td> s</td> <td> 115</td> </tr>
# <tr> <td> t</td> <td> 116</td> </tr>
# <tr> <td> u</td> <td> 117</td> </tr>
# <tr> <td> v</td> <td> 118</td> </tr>
# <tr> <td> w</td> <td> 119</td> </tr>
# <tr> <td> x</td> <td> 120</td> </tr>
# <tr> <td> y</td> <td> 121</td> </tr>
# <tr> <td> z</td> <td> 122</td> </tr>
# </table> </html>
