# -*- coding: utf-8 -*-
#
# 	Copyright (C) 2017 by Igor E. Novikov
#
# 	This program is free software: you can redistribute it and/or modify
# 	it under the terms of the GNU General Public License as published by
# 	the Free Software Foundation, either version 3 of the License, or
# 	(at your option) any later version.
#
# 	This program is distributed in the hope that it will be useful,
# 	but WITHOUT ANY WARRANTY; without even the implied warranty of
# 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# 	GNU General Public License for more details.
#
# 	You should have received a copy of the GNU General Public License
# 	along with this program.  If not, see <http://www.gnu.org/licenses/>.

import lcms2
import unittest, os

_pkgdir = os.path.dirname(__file__)

def get_filepath(filename):
	return os.path.join(_pkgdir, 'cms_data', filename)

class TestCmsFunctions(unittest.TestCase):

	def setUp(self):
		rgb_profile = get_filepath('sRGB.icm')
		self.inProfile = lcms2.cmsOpenProfileFromFile(rgb_profile)
		cmyk_profile = get_filepath('CMYK.icm')
		self.outProfile = lcms2.cmsOpenProfileFromFile(cmyk_profile)
		self.transform = lcms2.cmsCreateTransform(self.inProfile,
						lcms2.TYPE_RGBA_8, self.outProfile, lcms2.TYPE_CMYK_8,
						lcms2.INTENT_PERCEPTUAL, lcms2.cmsFLAGS_NOTPRECALC)
		self.transform2 = lcms2.cmsCreateTransform(self.inProfile,
						lcms2.TYPE_RGBA_8, self.outProfile, lcms2.TYPE_CMYK_8,
						lcms2.INTENT_PERCEPTUAL, 0)


	def tearDown(self):
		pass

	def test01_open_profile(self):
		self.assertNotEqual(None, self.inProfile)
		self.assertNotEqual(None, self.outProfile)

	def test02_create_srgb_profile(self):
		self.assertNotEqual(None, lcms2.cmsCreate_sRGBProfile())

	def test03_create_gray_profile(self):
		self.assertNotEqual(None, lcms2.cmsCreateGrayProfile())

	def test04_create_lab_profile(self):
		self.assertNotEqual(None, lcms2.cmsCreateLabProfile())

	def test05_create_xyz_profile(self):
		self.assertNotEqual(None, lcms2.cmsCreateXYZProfile())



def get_suite():
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(TestCmsFunctions))
	return suite


if __name__ == '__main__':
	unittest.TextTestRunner(verbosity=2).run(get_suite())
