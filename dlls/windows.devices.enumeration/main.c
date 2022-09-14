/* WinRT Windows.Devices.Enumeration implementation
 *
 * Copyright 2021 Gijs Vermeulen
 * Copyright 2022 Julian Klemann for CodeWeavers
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA
 */

#include "initguid.h"
#include "private.h"

#include "wine/debug.h"

WINE_DEFAULT_DEBUG_CHANNEL(enumeration);

static const char *debugstr_hstring( HSTRING hstr )
{
    const WCHAR *str;
    UINT32 len;
    if (hstr && !((ULONG_PTR)hstr >> 16)) return "(invalid)";
    str = WindowsGetStringRawBuffer( hstr, &len );
    return wine_dbgstr_wn( str, len );
}

struct device_information_statics
{
    IActivationFactory IActivationFactory_iface;
    IDeviceInformationStatics2 IDeviceInformationStatics2_iface;
    LONG ref;
};

static inline struct device_information_statics *impl_from_IActivationFactory( IActivationFactory *iface )
{
    return CONTAINING_RECORD( iface, struct device_information_statics, IActivationFactory_iface );
}

static HRESULT WINAPI activation_factory_QueryInterface( IActivationFactory *iface, REFIID iid, void **out )
{
    struct device_information_statics *impl = impl_from_IActivationFactory( iface );

    TRACE( "iface %p, iid %s, out %p stub!\n", iface, debugstr_guid( iid ), out );

    if (IsEqualGUID( iid, &IID_IUnknown ) ||
        IsEqualGUID( iid, &IID_IInspectable ) ||
        IsEqualGUID( iid, &IID_IActivationFactory ))
    {
        IInspectable_AddRef( (*out = &impl->IActivationFactory_iface) );
        return S_OK;
    }

    if (IsEqualGUID( iid, &IID_IDeviceInformationStatics2 ))
    {
        IInspectable_AddRef( (*out = &impl->IDeviceInformationStatics2_iface) );
        return S_OK;
    }

    FIXME( "%s not implemented, returning E_NOINTERFACE.\n", debugstr_guid( iid ) );
    *out = NULL;
    return E_NOINTERFACE;
}

static ULONG WINAPI activation_factory_AddRef( IActivationFactory *iface )
{
    struct device_information_statics *impl = impl_from_IActivationFactory( iface );
    ULONG ref = InterlockedIncrement( &impl->ref );
    TRACE( "iface %p, ref %lu.\n", iface, ref );
    return ref;
}

static ULONG WINAPI activation_factory_Release( IActivationFactory *iface )
{
    struct device_information_statics *impl = impl_from_IActivationFactory( iface );
    ULONG ref = InterlockedDecrement( &impl->ref );
    TRACE( "iface %p, ref %lu.\n", iface, ref );
    return ref;
}

static HRESULT WINAPI activation_factory_GetIids( IActivationFactory *iface, ULONG *iid_count, IID **iids )
{
    FIXME( "iface %p, iid_count %p, iids %p stub!\n", iface, iid_count, iids );
    return E_NOTIMPL;
}

static HRESULT WINAPI activation_factory_GetRuntimeClassName( IActivationFactory *iface, HSTRING *class_name )
{
    FIXME( "iface %p, class_name %p stub!\n", iface, class_name );
    return E_NOTIMPL;
}

static HRESULT WINAPI activation_factory_GetTrustLevel( IActivationFactory *iface, TrustLevel *trust_level )
{
    FIXME( "iface %p, trust_level %p stub!\n", iface, trust_level );
    return E_NOTIMPL;
}

static HRESULT WINAPI activation_factory_ActivateInstance( IActivationFactory *iface, IInspectable **instance )
{
    FIXME( "iface %p, instance %p stub!\n", iface, instance );
    return E_NOTIMPL;
}

static const struct IActivationFactoryVtbl activation_factory_vtbl =
{
    activation_factory_QueryInterface,
    activation_factory_AddRef,
    activation_factory_Release,
    /* IInspectable methods */
    activation_factory_GetIids,
    activation_factory_GetRuntimeClassName,
    activation_factory_GetTrustLevel,
    /* IActivationFactory methods */
    activation_factory_ActivateInstance,
};

DEFINE_IINSPECTABLE( device_statics2, IDeviceInformationStatics2, struct device_information_statics, IActivationFactory_iface );

static HRESULT WINAPI device_statics2_GetAqsFilterFromDeviceClass( IDeviceInformationStatics2 *iface, DeviceClass device_class,
                                                                   HSTRING *filter )
{
    FIXME( "iface %p, device_class %u, filter %p stub!\n", iface, device_class, filter );
    return E_NOTIMPL;
}

static HRESULT WINAPI device_statics2_CreateFromIdAsync( IDeviceInformationStatics2 *iface, HSTRING device_id,
                                                         IIterable_HSTRING *additional_properties, DeviceInformationKind kind,
                                                         IAsyncOperation_DeviceInformation **async_operation )
{
    FIXME( "iface %p, device_id %s, additional_properties %p, kind %u, async_operation %p stub!\n",
            iface, debugstr_hstring( device_id ), additional_properties, kind, async_operation );
    return E_NOTIMPL;
}

static HRESULT WINAPI device_statics2_FindAllAsync( IDeviceInformationStatics2 *iface, HSTRING filter,
                                                    IIterable_HSTRING *additional_properties, DeviceInformationKind kind,
                                                    IAsyncOperation_DeviceInformationCollection **async_operation )
{
    FIXME( "iface %p, filter %s, additional_properties %p, kind %u, async_operation %p stub!\n",
            iface, debugstr_hstring( filter ), additional_properties, kind, async_operation );
    return E_NOTIMPL;
}

static HRESULT WINAPI device_statics2_CreateWatcher( IDeviceInformationStatics2 *iface, HSTRING filter,
                                                     IIterable_HSTRING *additional_properties, DeviceInformationKind kind,
                                                     IDeviceWatcher **watcher )
{
    FIXME( "iface %p, filter %s, additional_properties %p, kind %u, watcher %p stub!\n",
            iface, debugstr_hstring( filter ), additional_properties, kind, watcher );
    return E_NOTIMPL;
}

static const struct IDeviceInformationStatics2Vtbl device_statics2_vtbl =
{
    device_statics2_QueryInterface,
    device_statics2_AddRef,
    device_statics2_Release,
    /* IInspectable methods */
    device_statics2_GetIids,
    device_statics2_GetRuntimeClassName,
    device_statics2_GetTrustLevel,
    /* IDeviceInformationStatics2 methods */
    device_statics2_GetAqsFilterFromDeviceClass,
    device_statics2_CreateFromIdAsync,
    device_statics2_FindAllAsync,
    device_statics2_CreateWatcher
};

static struct device_information_statics device_information_statics =
{
    {&activation_factory_vtbl},
    {&device_statics2_vtbl},
    1
};

HRESULT WINAPI DllGetClassObject( REFCLSID clsid, REFIID riid, void **out )
{
    FIXME( "clsid %s, riid %s, out %p stub!\n", debugstr_guid( clsid ), debugstr_guid( riid ), out );
    return CLASS_E_CLASSNOTAVAILABLE;
}

HRESULT WINAPI DllGetActivationFactory( HSTRING classid, IActivationFactory **factory )
{
    TRACE( "classid %s, factory %p.\n", debugstr_hstring( classid ), factory );
    *factory = &device_information_statics.IActivationFactory_iface;
    IUnknown_AddRef( *factory );
    return S_OK;
}
