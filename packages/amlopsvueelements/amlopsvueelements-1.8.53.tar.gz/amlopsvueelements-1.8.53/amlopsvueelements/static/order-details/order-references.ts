import Api from '@/services';
import { getIsAdmin } from '@/helpers';

import type { IAircraftLocations, IAirportLocations, IRecentFlightsResponse } from 'shared/types';
import type { ISupplierFuelDetails } from 'shared/types';
import type { IFuelPricingObj, ISupplierFuel } from 'shared/types';
import type { IPaginatedResponse, ITypeReference } from '@/types/general.types';
import type { IAircraft, IAircraftTypeEntity } from '@/types/order/aircraft.types';
import type { IAirport } from '@/types/order/airport.types';
import type {
  IClient,
  IGroundHandler,
  IOperator,
  IOrder,
  IOrderNote,
  IOrderStatus,
  IOrderType
} from '@/types/order/order.types';
import type {
  IFuelUnit,
  IOrderRoi,
  IOrganisation,
  IPerson,
  IService
} from '@/types/order/order-reference.types';
// import type { ISupplierFuelDetails } from 'shared/types';

class OrderReferenceService extends Api {
  async fetchOrderStatuses() {
    const { data } = await this.get<IOrderStatus[]>(`api/v1/orders/order_statuses/?search=`);
    return data && typeof data === 'object' ? data : [];
  }

  async fetchOrderTypes() {
    const { data } = await this.get<IOrderType[]>(`api/v1/orders/order_types/`);
    return data;
  }

  async fetchOrganisations(search?: string) {
    const {
      data: { results: organisations }
    } = await this.get<IPaginatedResponse<IOrganisation[]>>('api/v1/admin/organisations/', {
      params: { search, 'page[size]': 999 }
    });
    return organisations;
  }

  async fetchOrganisationPeople(organisationId: number) {
    if (!organisationId) return [];
    const url = `api/v1/organisations/${organisationId}/people/`;
    const { data } = await this.get<IPerson[]>(url);
    return data.map((item) => ({
      ...item,
      display: `${item.details.full_name} (${item.jobs[0]?.job_title})`,
      display_email: `${item.details.full_name} ${item.details.contact_email}`
    }));
  }

  async fetchAircraftTypes(organisationId: number) {
    if (getIsAdmin() && !organisationId) return [];
    const url = getIsAdmin()
      ? `api/v1/admin/organisation/${organisationId}/aircraft_types/`
      : `api/v1/organisation/aircraft_types/`;
    const {
      data: { data }
    } = await this.get<{ data: IAircraftTypeEntity[] }>(url);
    return data.map((el) => ({
      ...el,
      full_repr: `${el.attributes.manufacturer} ${el.attributes.model} (${el.attributes.designator})`
    }));
  }

  async fetchAircrafts(organisationId: number) {
    if (!organisationId) return [];
    const url = `api/v1/aircraft/`;
    const { data } = await this.get<IAircraft[]>(url, {
      params: { operator: organisationId }
    });
    return data;
  }

  async fetchAirportLocations(search?: string | number) {
    const {
      data: { results: airports }
    } = await this.get<IPaginatedResponse<IAirport[]>>('api/v1/organisations/', {
      params: {
        search,
        type: 8,
        optional_fields: 'country'
      }
    });
    return airports;
  }

  async fetchFuelQuantityUnits() {
    const { data } = await this.get<IFuelUnit[]>('api/v1/uom/');
    return data;
  }

  async fetchFuelCategories() {
    const { data } = await this.get<ITypeReference[]>('api/v1/fuel_categories/');
    return data;
  }

  async fetchGroundHandlers(airportId: number) {
    const {
      data: { results: handlers }
    } = await this.get<IPaginatedResponse<IGroundHandler[]>>('api/v1/organisations/', {
      params: {
        type: 3,
        gh_location: airportId
      }
    });
    return handlers;
  }

  async fetchClients() {
    const {
      data: { results: clients }
    } = await this.get<IPaginatedResponse<IClient[]>>('api/v1/organisations/', {
      params: {
        type_str: 'client',
        optional_fields: 'client_status_list'
      }
    });
    return clients;
  }

  async fetchOperators() {
    const {
      data: { results: operators }
    } = await this.get<IPaginatedResponse<IOperator[]>>('api/v1/organisations/', {
      params: {
        type_str: 'operator'
      }
    });
    return operators;
  }

  async fetchMissionTypes() {
    const { data } = await this.get<ITypeReference[]>('api/v1/admin/handling_requests/types/');
    return data;
  }

  async fetchPersonTitles() {
    const { data } = await this.get<ITypeReference[]>('api/v1/person_titles/');
    return data;
  }

  async fetchPersonRoles() {
    const { data } = await this.get<ITypeReference[]>('api/v1/person_roles/');
    return data;
  }

  async fetchServices(
    locationId?: string | number,
    organisationId?: string | number,
    codeName?: string
  ) {
    const { data } = await this.get<{ data: IService[] }>('api/v1/handling_services/', {
      params: { organisation_id: organisationId, location_id: locationId, codename: codeName }
    });
    return data.data
      ?.filter((service) => {
        return !(
          service.attributes.is_dla &&
          !service.attributes.is_dla_visible_arrival &&
          !service.attributes.is_dla_visible_departure
        );
      })
      .map((service) => ({
        ...service,
        id: Number(service.id)
      }));
  }

  async fetchMeta() {
    const { data } = await this.get('api/v1/meta/');
    return data;
  }

  async fetchOrderNotes(orderId: number) {
    const { data } = await this.get<IOrderNote[]>(`api/v1/orders/${orderId}/notes/`);
    return data;
  }

  async fetchSupplierFuel(
    orderPricingCalculationRecord: IOrder['pricing_calculation_record']
  ): Promise<ISupplierFuel> {
    const { data } = await this.get<ISupplierFuel>(
      `api/v1/pricing/supplier_fuel_pricing/${orderPricingCalculationRecord}/`
    );
    return data;
  }

  async fetchSupplierFuelDetails(
    supplierId: number,
    detailsId: number
  ): Promise<ISupplierFuelDetails> {
    const { data } = await this.get<ISupplierFuelDetails>(
      `api/v1/pricing/supplier_fuel_pricing/${supplierId}/results/${detailsId}/`
    );
    return data;
  }

  async selectFuelSupplier(orderId: number, payload: any) {
    const { data } = await this.post<any[]>(
      `api/v1/orders/${orderId}/fuel_pricing/from_pricing_record/`,
      payload
    );
    return data;
  }

  async fetchOrderPricing(orderId: number): Promise<IFuelPricingObj> {
    const { data } = await this.get<any>(`api/v1/orders/${orderId}/fuel_pricing/`);
    return data;
  }

  async updateOrderPricing(orderId: number, payload: any): Promise<IFuelPricingObj> {
    const { data } = await this.put<IFuelPricingObj>(
      `api/v1/orders/${orderId}/fuel_pricing/`,
      payload
    );
    return data;
  }

  async updateOrderROI(orderId: number, payload: any) {
    const { data } = await this.post<IOrderRoi>(`api/v1/orders/${orderId}/roi/`, payload);
    return data;
  }

  async fetchFlightAirportLocations(id: number): Promise<IAirportLocations> {
    const { data } = await this.post<any>(`api/v1/sfr_tracking/airport_locations/`, {
      handling_request: id.toString()
    });
    return data;
  }

  async fetchFlightAircraftLocations(id: number): Promise<IAircraftLocations> {
    const { data } = await this.post<any>(`api/v1/sfr_tracking/aircraft_locations/`, {
      handling_request: id.toString()
    });
    return data;
  }

  async fetchOrderQuoteButton(orderId: number) {
    const { data } = await this.get<any>(`api/v1/orders/${orderId}/quote_button/`);
    return data;
  }

  async fetchOrderProceedButton(orderId: number) {
    const { data } = await this.get<any>(`api/v1/orders/${orderId}/proceed_button/`);
    return data;
  }

  async fetchRecentFlights(orderId: number) {
    const { data } = await this.get<IRecentFlightsResponse>(
      `api/v1/orders/${orderId}/recent_flights/`
    );
    return typeof data === 'object' ? data : null;
  }

  async fetchHandlingServices() {
    const { data } = await this.get<any>(`api/v1/handling_services/`);
    return typeof data === 'object' ? data : null;
  }
}

export default new OrderReferenceService();
