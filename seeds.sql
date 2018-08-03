-- Role --
INSERT INTO public.roles (id, "name", created_at, updated_at) VALUES(1, 'Admin', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');

-- User --
INSERT INTO public.users (id, "name", email, password, is_active, is_confirm, confirmation_token, remember_token, avatar, role_id, is_authenticated, last_authenticated, created_at, updated_at) 
VALUES(1, 'Admin', 'admin@admin.com', 'pbkdf2:sha256:50000$dl41vHyC$349b7c84072ea50e0c733c84e60c41cbde7e42093831b0e968156d3bab8def5f', true, true, '', '', NULL, 1, true, '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342', '2018-08-03 06:18:40.649');

-- Menu --
INSERT INTO public.menus (id, label, target, parent_id, "position", "group", is_active, user_id, created_at, updated_at, icon) VALUES(1, 'Dashboard', '/', NULL, 0, 'admin.sidebar', true, 1, '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342', 'fa fa-dashboard');
INSERT INTO public.menus (id, label, target, parent_id, "position", "group", is_active, user_id, created_at, updated_at, icon) VALUES(3, 'Page', '/page/', NULL, 2, 'admin.sidebar', true, 1, '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342', 'fa fa-file');
INSERT INTO public.menus (id, label, target, parent_id, "position", "group", is_active, user_id, created_at, updated_at, icon) VALUES(5, 'Role', '/role/', NULL, 4, 'admin.sidebar', true, 1, '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342', 'fa fa-file');
INSERT INTO public.menus (id, label, target, parent_id, "position", "group", is_active, user_id, created_at, updated_at, icon) VALUES(4, 'User', '/user/', NULL, 3, 'admin.sidebar', true, 1, '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342', 'fa fa-user');
INSERT INTO public.menus (id, label, target, parent_id, "position", "group", is_active, user_id, created_at, updated_at, icon) VALUES(2, 'Menu', '/menu/', NULL, 1, 'admin.sidebar', true, 1, '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342', 'fa fa-th');

-- Permission --
INSERT INTO public.permissions (id, "name", "group", created_at, updated_at) VALUES(1, 'page.index', 'Page', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions (id, "name", "group", created_at, updated_at) VALUES(2, 'page.create', 'Page', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions (id, "name", "group", created_at, updated_at) VALUES(3, 'page.edit', 'Page', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions (id, "name", "group", created_at, updated_at) VALUES(4, 'page.delete', 'Page', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions (id, "name", "group", created_at, updated_at) VALUES(5, 'menu.index', 'Menu', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions (id, "name", "group", created_at, updated_at) VALUES(6, 'menu.create', 'Menu', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions (id, "name", "group", created_at, updated_at) VALUES(7, 'menu.edit', 'Menu', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions (id, "name", "group", created_at, updated_at) VALUES(8, 'menu.delete', 'Menu', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions (id, "name", "group", created_at, updated_at) VALUES(9, 'user.index', 'User', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions (id, "name", "group", created_at, updated_at) VALUES(10, 'user.create', 'User', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions (id, "name", "group", created_at, updated_at) VALUES(11, 'user.edit', 'User', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions (id, "name", "group", created_at, updated_at) VALUES(12, 'user.delete', 'User', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions (id, "name", "group", created_at, updated_at) VALUES(13, 'role.index', 'Role', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions (id, "name", "group", created_at, updated_at) VALUES(14, 'role.create', 'Role', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions (id, "name", "group", created_at, updated_at) VALUES(15, 'role.edit', 'Role', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions (id, "name", "group", created_at, updated_at) VALUES(16, 'role.delete', 'Role', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');
INSERT INTO public.permissions (id, "name", "group", created_at, updated_at) VALUES(17, '.index', 'Dashboard', '2018-08-03 06:40:07.342', '2018-08-03 06:40:07.342');

-- Role Permission --
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 1, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 2, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 3, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 4, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 5, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 6, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 7, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 8, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 9, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 10, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 11, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 12, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 13, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 14, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 15, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 16, '2018-08-03 06:40:07.342');
INSERT INTO public.role_permission (role_id, permission_id, attached_at) VALUES(1, 17, '2018-08-03 06:40:07.342');
