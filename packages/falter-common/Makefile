# Copyright (C) 2011 Manuel Munz <freifunk at somakoma de>
# This is free software, licensed under the Apache 2.0 license.

include $(TOPDIR)/rules.mk

PKG_NAME:=falter-common
PKG_RELEASE:=2

PKG_BUILD_DIR := $(BUILD_DIR)/$(PKG_NAME)

include $(INCLUDE_DIR)/package.mk

define Package/falter-common
  SECTION:=luci
  CATEGORY:=LuCI
  SUBMENU:=9. Freifunk
  TITLE:=Falter common files
  EXTRA_DEPENDS:=uci
endef

define Package/falter-common/description
  Common files and scripts that are needed to run free wireless mesh networks.
endef

define Package/falter-common/conffiles
/etc/config/freifunk
endef

define Package/falter-common-olsr
  SECTION:=luci
  CATEGORY:=LuCI
  SUBMENU:=9. Freifunk
  TITLE:=Falter common files for olsr-v1
  EXTRA_DEPENDS:=falter-common, olsrd, micrond, libuci-lua, lua
endef

define Package/falter-common-olsr/description
  Additional files and scripts that are needed to run free wireless mesh networks based on OLSRv1.
endef

define Build/Prepare
	mkdir -p $(PKG_BUILD_DIR)
endef

define Build/Configure
endef

define Build/Compile
endef

define Package/falter-common/install
	$(CP) ./files-common/* $(1)/
endef

define Package/falter-common-olsr/install
	$(CP) ./files-olsrv1/* $(1)/
endef

$(eval $(call BuildPackage,falter-common))
$(eval $(call BuildPackage,falter-common-olsr))
