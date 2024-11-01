/* SPDX-License-Identifier: LGPL-3.0-or-later */

/*
 * Copyright (C) 2023 Perry Werneck <perry.werneck@gmail.com>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published
 * by the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

/*
 * Based on dmidecode
 *
 * Copyright (C) 2000-2002 Alan Cox <alan@redhat.com>
 * Copyright (C) 2002-2020 Jean Delvare <jdelvare@suse.de>
 *
 */

 /**
  * @brief Implement chassis decoders.
  */

 #ifdef HAVE_CONFIG_H
	#include <config.h>
 #endif // HAVE_CONFIG_H

 #include <private/decoders.h>
 #include <private/decoders/tools.h>
 #include <private/decoders/chassis.h>
 #include <smbios/node.h>
 #include <iostream>
 #include <string>
 #include <cstring>

 using namespace std;

 namespace SMBios {

	std::string Decoder::ChassisState::as_string(const Node::Header &header, const uint8_t *ptr, const size_t offset) const {

		static const char *state[] = {
			"Other", /* 0x01 */
			"Unknown",
			"Safe",
			"Warning",
			"Critical",
			"Non-recoverable" /* 0x06 */
		};

		auto code = as_uint(header,ptr,offset);

		if (code >= 0x01 && code <= 0x06)
			return state[code - 0x01];

		return "";
	}

	unsigned int Decoder::ChassisType::as_uint(const Node::Header &header, const uint8_t *data, const size_t offset) const {

		if(offset > header.length) {
			return 0;
		}

		return (data[offset] & 0x7F); // bits 6:0 are chassis type, 7th bit is the lock bit

	}

	std::string Decoder::ChassisType::as_string(const Node::Header &header, const uint8_t *ptr, const size_t offset) const {

		static const char *type[] = {
			"Other", // 0x01
			"Unknown",
			"Desktop",
			"Low Profile Desktop",
			"Pizza Box",
			"Mini Tower",
			"Tower",
			"Portable",
			"Laptop",
			"Notebook",
			"Hand Held",
			"Docking Station",
			"All In One",
			"Sub Notebook",
			"Space-saving",
			"Lunch Box",
			"Main Server Chassis", // CIM_Chassis.ChassisPackageType says "Main System Chassis"
			"Expansion Chassis",
			"Sub Chassis",
			"Bus Expansion Chassis",
			"Peripheral Chassis",
			"RAID Chassis",
			"Rack Mount Chassis",
			"Sealed-case PC",
			"Multi-system",
			"CompactPCI",
			"AdvancedTCA",
			"Blade",
			"Blade Enclosing",
			"Tablet",
			"Convertible",
			"Detachable",
			"IoT Gateway",
			"Embedded PC",
			"Mini PC",
			"Stick PC" // 0x24
		};

		auto code = as_uint(header, ptr, offset);

		if (code >= 0x01 && code <= 0x24)
			return type[code - 0x01];

		return "";
	}

	unsigned int Decoder::ChassisLock::as_uint(const Node::Header &header, const uint8_t *data, const size_t offset) const {
		if(offset > header.length) {
			return 0;
		}
		return (unsigned int) (data[offset] >> 7);
	}

	std::string Decoder::ChassisLock::as_string(const Node::Header &header, const uint8_t *ptr, const size_t offset) const {

		static const char *state[] = {
			"Not Present",	// 0x00
			"Present",		// 0x01
		};

		if(offset > header.length) {
			return "";
		}

		auto code = as_uint(header,ptr,offset);

		if (code <= 0x01)
			return state[code];

		return "";

	}

	std::string Decoder::ChassisSecurityStatus::as_string(const Node::Header &header, const uint8_t *ptr, const size_t offset) const {

		auto code = as_uint(header,ptr,offset);

		static const char *status[] = {
			"Other", // 0x01
			"Unknown",
			"None",
			"External Interface Locked Out",
			"External Interface Enabled" // 0x05
		};

		if (code >= 0x01 && code <= 0x05)
			return status[code - 0x01];

		return "";

	}

	unsigned int Decoder::ChassisOEMInformation::as_uint(const Node::Header &header, const uint8_t *ptr, const size_t offset) const {

		if(header.length < 0x11) {
			return 0;
		}

		return Hex16::as_uint(header,ptr,offset);
	}

	std::string Decoder::ChassisOEMInformation::as_string(const Node::Header &header, const uint8_t *ptr, const size_t offset) const {

		if(header.length < 0x11) {
			return "";
		}

		return Hex16::as_string(header,ptr,offset);
	}

	unsigned int Decoder::ChassisHeight::as_uint(const Node::Header &header, const uint8_t *ptr, const size_t offset) const {

		if (header.length < 0x13) {
			return 0;
		}

		return (unsigned int) ptr[offset];
	}

	std::string Decoder::ChassisHeight::as_string(const Node::Header &header, const uint8_t *ptr, const size_t offset) const {

		if (header.length < 0x13) {
			return "";
		}

		unsigned int code = as_uint(header,ptr,offset);

		if(!code) {
			return "Unspecified";
		}

		std::string str{std::to_string(code)};
		str += " U";

		return str;
	}

 }

