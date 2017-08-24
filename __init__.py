# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SpiderWebBuilder
                                 A QGIS plugin
 Evakuierungsspinnennetz
                             -------------------
        begin                : 2017-08-24
        copyright            : (C) 2017 by Ulrich Meier
        email                : uli@meier-tkn.de
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SpiderWebBuilder class from file SpiderWebBuilder.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .spider_web_builder import SpiderWebBuilder
    return SpiderWebBuilder(iface)
