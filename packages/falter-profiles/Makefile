# Copyright (C) 2011 Manuel Munz <freifunk at somakoma de>
# This is free software, licensed under the Apache 2.0 license.

include $(TOPDIR)/rules.mk

PKG_NAME:=falter-profiles
PKG_RELEASE:=1

PKG_BUILD_DIR := $(BUILD_DIR)/$(PKG_NAME)

PKG_SOURCE_PROTO:=git 
PKG_SOURCE_URL:=https://github.com/freifunk/openwrt-packages.git
PKG_SOURCE_VERSION:=master

include $(INCLUDE_DIR)/package.mk

define Package/falter-profiles
  SECTION:=luci
  CATEGORY:=LuCI
  SUBMENU:=9. Freifunk
  TITLE:=Falter profiles
  EXTRA_DEPENDS:=falter-common
  PKGARCH:=all
endef

define Package/falter-profiles/description
  These falter profiles set defaults for various free network/freifunk communities and are used by wizards like ffwizard and meshwizard.
endef

# only download the profiles from Freifunk/openwrt-packages. This is only pssible with svn.
define Build/Prepare
	mkdir -p $(PKG_BUILD_DIR)/files
	$(CP) $(PKG_BUILD_DIR)/contrib/package/community-profiles/files/* $(PKG_BUILD_DIR)/files/
endef

define Build/Configure
endef

define Build/Compile
endef

define Package/falter-profiles/install
	$(CP) $(PKG_BUILD_DIR)/files/* $(1)/
endef

$(eval $(call BuildPackage,falter-profiles))
