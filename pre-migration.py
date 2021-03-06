# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Akretion (http://www.akretion.com/)
#    @author: Alexis de Lattre <alexis.delattre@akretion.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


def migrate(cr, version):
    if not version:
        return

    cr.execute(
        'ALTER TABLE "account_cutoff_line" RENAME "after_cutoff_days" '
        'TO "prepaid_days"')

    cr.execute(
        "UPDATE payment_line SET communication = communication2, "
        "communication2 = null "
        "FROM payment_order "
        "WHERE payment_line.order_id = payment_order.id "
        "AND payment_order.state in ('draft', 'open') "
        "AND payment_line.state = 'normal' "
        "AND communication2 is not null")

# Explications :
# Il faut créer un sous-répertoire "migrations/7.0.0.2/" et mettre ce script dedans:
# le script sera alors exécuté pour openerp 7.0, quand on met à jour le module vers la version 0.2
