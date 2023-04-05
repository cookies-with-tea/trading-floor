import { configure, fireEvent, getByTestId, queryByTestId } from '@testing-library/vue';
import { expect, test } from 'vitest';
import { mount } from '@vue/test-utils';
import CInput from '@/components/common/CInput/CInput.vue';

configure({ testIdAttribute: 'data-tid' });

//PO - PageObject
// eslint-disable-next-line @typescript-eslint/no-unused-vars
const CInputPO = {
  click() {
    fireEvent.click(getByTestId(document.body, 'c-input'));
  },
  getComponent() {
    return queryByTestId(document.body, 'c-input');
  },
};

test('CInput Snapshot', () => {
  const wrapper = mount(CInput, {
    props: { modelValue: 'snapshot' },
  });

  expect(wrapper.element).toMatchSnapshot();
});
